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
    except:
        pass