#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from utils.control import start, stop, get_log, get_config, update_config, status

if __name__ == '__main__':
    start()


    class RequestHandler(SimpleXMLRPCRequestHandler):
        rpc_paths = ('/RPC2',)


    # Create server
    with SimpleXMLRPCServer(("localhost", 29869),
                            requestHandler=RequestHandler) as server:
        server.register_introspection_functions()

        server.register_function(start)
        server.register_function(stop)
        server.register_function(get_log)
        server.register_function(get_config)
        server.register_function(update_config)
        server.register_function(status)

        # Run the server's main loop
        server.serve_forever()
