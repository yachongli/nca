import eventlet
from oslo_log import log
from nca import service

LOG = log.getLogger(__name__)


def eventlet_wsgi_server():
    nca_api = service.serve_wsgi(service.NcaApiService)
    start_api_and_rpc_worker(nca_api)


def start_api_and_rpc_worker(nca_api):
    try:
        worker_launcher = service.start_all_workers()

        pool = eventlet.GreenPool()
        api_thread = pool.spawn(nca_api.wait)
        plugin_workers_thread = pool.spawn(worker_launcher.wait)

        # api and other workers should die together. When one dies,
        # kill the other.
        api_thread.link(lambda gt: plugin_workers_thread.kill())
        plugin_workers_thread.link(lambda gt: api_thread.kill())

        pool.waitall()
    except NotImplementedError:
        LOG.info("RPC was already started in parent process by "
                 "plugin.")

        nca_api.wait()
