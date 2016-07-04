#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Tobias'

import BaseHTTPServer

class MyHTTPServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print "Got GET Request from ", self.client_address
        self.wfile.write('Sorry, I do not speak HTTP\r\nMarkus ist dumm')

server_address = ('', 9080)
handler_class = MyHTTPServer
server_class = BaseHTTPServer.HTTPServer

server = server_class(server_address, handler_class)
server.serve_forever()