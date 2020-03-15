#!/usr/bin/env python3
# webserver.py - a webserver which draws the temperature
import mimetypes
import http.server

import io
import os
from datetime import datetime
import rrdtool

IMAGE_BUFFER = io.BytesIO()
LAST_MODIFIED_DATE = None
LAST_CALL = None

class TemperatureServer(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        path_list = path.split('/')
        if path_list[1] == 'favicon.ico':
            self.send_file('graph/temperature.ico')
            return
        if path_list[1].startswith('stats.txt'):
            params = path_list[1].split('?')
            if len(params) == 1:
                self.send_stats(params[0])
            else:
                self.send_stats(params[0], params[1])
            return
        if path_list[1].startswith('graph'):
            self.send_file('/'.join(path_list[1:]))
            return
        if len(path_list) == 1:
            self.send_error()
            return

        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()


    def send_error(self):
        self.send_response(403)
        self.end_headers()
        self.wfile.write('Illegal syntax. '
                         'Use ?{all,date?date1?date2,game?num}'
                         '\r\n')
        self.wfile.write('Input: ' + self.path + '\r\n')
    
    def read_stats(self):
        with open('stats.txt') as s_file:
            self.lines = s_file.readlines()

    def send_stats(self, filepath, params=None):
        self.send_response(200)
        self.send_header("Content-type", 'text')
        self.end_headers()
        
        if params:
          rrdtool_params = []
          for param in params.split('&'):
            splitted = param.split('=')
            rrdtool_params.append('--' + splitted[0])
            if len(splitted) == 2:
              rrdtool_params.append(splitted[1])
          print(rrdtool_params)
          start_stop, names, data = rrdtool.fetch('values.rrd', 'AVERAGE', *rrdtool_params)
        else:
          start_stop, names, data = rrdtool.fetch('values.rrd', 'AVERAGE', 
                                                  '--start', 'end-2days')
        
        for index in range(len(data)):
            time = start_stop[0] + index * start_stop[2]
            self.wfile.write(bytes("{}, {}, {}, {}, {}\n".format(time, data[index][0], data[index][1], data[index][2], data[index][3]), 'utf-8'))
        

    def send_file(self, filepath, last_lines=-1):
        self.send_response(200)
        filepath = filepath.split('?')[0]
        content_type = mimetypes.guess_type(filepath)[0]

        self.send_header("Content-type", content_type)
        self.send_header("Cache-Control", "public")
        self.end_headers()
        image_file = open(filepath, 'rb')
        if last_lines == -1:
            self.wfile.write(image_file.read())
        else:
            lines = image_file.read().split('\n')
            for line in lines[-last_lines:]:
                self.wfile.write(line + '\n')

def run_server(port=9090):
    server_class = http.server.HTTPServer
    server_address = ('', port)
    handler_class = TemperatureServer

    server = server_class(server_address, handler_class)
    server.serve_forever()

if __name__ == '__main__':
    path = '/home/pi/temperature-webserver'
    try:
        os.chdir(path)
    except OSError:
        print(('Cannot change to folder: {0}'.format(path)))
    run_server(port=50)
