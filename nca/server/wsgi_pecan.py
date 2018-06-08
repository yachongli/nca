from oslo_log import log
from nca._i18n import _LI
from nca.pecan_wsgi import app as pecan_app
from neutron.server import wsgi_eventlet
from nca import service

LOG = log.getLogger(__name__)

def pecan_wsgi_server():
    LOG.info(_LI("Pecan WSGI server starting..."))
    application = pecan_app.setup_app()
    nca_api = service.run_wsgi_app(application)
    wsgi_eventlet.start_api_and_rpc_workers(nca_api)