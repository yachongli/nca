from nca import server
from nca.server import rpc_eventlet
from nca.server import wsgi_eventlet

def main():
    server.boot_server(wsgi_eventlet.eventlet_wsgi_server)

def main_rpc_eventlet():
    server.boot_server(rpc_eventlet.eventlet_rpc_server)