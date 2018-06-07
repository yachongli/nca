from neutron_lib.callbacks import registry
from neutron_lib.callbacks import resources
from neutron_lib.callbacks import events
from oslo_config import cfg
from oslo_log import log as logging
from oslo_service import wsgi
from oslo_concurrency import processutils
from oslo_utils import excutils

from nca.common import profiler
from nca.common import config

LOG = logging.getLogger(__name__)


class WsgiService(object):
    def __init__(self, app_name):
        self.app_name = app_name
        self.wsgi_app = None

    def start(self):
        self.wsgi_app = _run_wsgi(self.app_name)

    def wait(self):
        self.wsgi_app.wait()


class NcaApiService(WsgiService):
    """Class for nca-api service"""

    def __init__(self, app_name):
        profiler.setup("nca_server", cfg.CONF.host)
        super(NcaApiService, self).__init__(app_name)

    @classmethod
    def create(cls, app_name):
        # Setup logging early
        config.setup_logging()
        service = cls(app_name)
        return service


def _run_wsgi(app_name):
    app = config.load_paste_app(app_name)
    if not app:
        LOG.error("No known Api cations configured.")
        return
    return run_wsgi_app(app)


def run_wsgi_app(app):
    server = wsgi.Server("Nca")
    server.start(app, cfg.CONF.bind_port, cfg.CONF.bind_host,
                 workers=_get_api_workers())
    LOG.info("nca service started, listening on %(host)s:%(port)s",
             {'host': cfg.CONF.bind_host, 'port': cfg.CONF.bind_port})
    return server


def _get_api_workers():
    workers = cfg.CONF.api_workers
    if workers is None:
        workers = processutils.get_worker_count()
    return workers


def serve_wsgi(cls):
    try:
        service = cls.create()
        service.start()
    except Exception:
        with excutils.save_and_reraise_exception():
            LOG.exception('Unrecoverable error: please check log '
                          'for details.')
    registry.publish(resources.PROCESS, events.BEFORE_SPAWN, service)
    return service

def start_all_workers():
    workers = _get_rpc_workers() + _get_plugins_workers()
    launcher = _start_workers(workers)