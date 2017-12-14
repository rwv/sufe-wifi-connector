#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from xmlrpc.server import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer

from utils.control import start, stop, get_log, get_config, update_config, get_status

if __name__ == '__main__':
    start()


    class RequestHandler(SimpleXMLRPCRequestHandler):
        """
        a SimpleXMLRPCRequestHandler instance that add OPTIONS methods
        """
        rpc_paths = ('/RPC2',)

        def do_OPTIONS(self):
            self.send_response(200)
            self.end_headers()

        # Add these headers to all responses
        def end_headers(self):
            self.send_header("Access-Control-Allow-Headers",
                             "Origin, X-Requested-With, Content-Type, Accept")
            self.send_header("Access-Control-Allow-Origin", "*")
            SimpleXMLRPCRequestHandler.end_headers(self)


    # Create server
    with SimpleXMLRPCServer(("localhost", 29869),
                            requestHandler=RequestHandler) as server:
        server.register_introspection_functions()

        server.register_function(start)
        server.register_function(stop)
        server.register_function(get_log)
        server.register_function(get_config)
        server.register_function(update_config)
        server.register_function(get_status)

        # Run the server's main loop
        print('RPC Server started.')
        server.serve_forever()
