#!/usr/bin/env python
# webserver.py - a webserver which draws stats of sauspiel
import mimetypes
import BaseHTTPServer
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import pylab
import io
import os
from datetime import datetime

IMAGE_BUFFER = io.BytesIO()
LAST_MODIFIED_DATE = None
LAST_CALL = None

class SauspielServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        path_list = path.split('/')
        if path_list[1] == 'favicon.ico':
            self.send_file('Stats.ico')
            return
        if path_list[1].startswith('stats.txt'):
            params = path_list[1].split('?')
            if len(params) == 1:
                self.send_file(params[0])
            else:
                self.send_file(params[0], last_lines=int(params[1]))
            return
        if path_list[1].startswith('graph'):
            self.send_file('/'.join(path_list[1:]))
            return
        if len(path_list) == 1:
            self.send_error()
            return
        self.op = path_list[1]
        # dummy, op, arg1, arg2 = lst

        if self.op not in ('all', 'date', 'game'):
            self.send_error()
            return

        if self.op == 'game':
            if len(path_list) != 3:
                self.send_error()
                return
            self.game_count = int(path_list[2])

        # self.read_stats()
        image_buffer = self.draw_plot()

        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()

        self.wfile.write(image_buffer.read())
        # image_buffer.close()
        # for line in self.lines[-5:]:
        #     self.wfile.write(line + '\r\n')
        # self.wfile.write(str(result) + '\r\n')

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

    def draw_plot(self):
        global LAST_CALL, LAST_MODIFIED_DATE, IMAGE_BUFFER
        data_filename = "stats.txt"
        try:
            mtime = os.path.getmtime(data_filename)
        except OSError:
            mtime = 0
        modified_date = datetime.fromtimestamp(mtime)
        if LAST_CALL == self.path and modified_date == LAST_MODIFIED_DATE:
            IMAGE_BUFFER.seek(0)
            return IMAGE_BUFFER
        LAST_CALL = self.path
        LAST_MODIFIED_DATE = modified_date
        data = pylab.genfromtxt(data_filename , delimiter=',', dtype=int)
        y_data = data[:, 0]
        x_data = data[:, 1]
        if self.op == 'game':
            y_data = y_data[-self.game_count:]
            x_data = x_data[-self.game_count:]
        pylab.plot(x_data, y_data, '-')
        # pylab.show()
        IMAGE_BUFFER = io.BytesIO()
        pylab.savefig(IMAGE_BUFFER, format='png')
        IMAGE_BUFFER.seek(0)
        # pylab.legend()
        # pylab.title("Title of Plot")
        # pylab.xlabel("X Axis Label")
        # pylab.ylabel("Y Axis Label")
        pylab.close()
        return IMAGE_BUFFER

    def send_file(self, filepath, last_lines=-1):
        self.send_response(200)
        filepath = filepath.split('?')[0]
        content_type = mimetypes.guess_type(filepath)[0]

        self.send_header("Content-type", content_type)
        self.end_headers()
        image_file = open(filepath)
        if last_lines == -1:
            self.wfile.write(image_file.read())
        else:
            lines = image_file.read().split('\n')
            for line in lines[-last_lines:]:
                self.wfile.write(line + '\n')

def run_server(port=9090):
    server_class = BaseHTTPServer.HTTPServer
    server_address = ('', port)
    handler_class = SauspielServer

    server = server_class(server_address, handler_class)
    server.serve_forever()

if __name__ == '__main__':
    path = '/home/pi/sauspiel/'
    try:
        os.chdir(path)
    except OSError:
        print('Cannot change to folder: {0}'.format(path))
    run_server(port=50)
