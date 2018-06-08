from nca import server
from nca.server import rpc_eventlet
from nca.server import wsgi_eventlet
from nca.server import wsgi_pecan

def main():
    server.boot_server(wsgi_pecan.pecan_wsgi_server)

def main_rpc_eventlet():
    server.boot_server(rpc_eventlet.eventlet_rpc_server)

if __name__ == '__main__':
    main()