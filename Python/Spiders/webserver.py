#!/usr/bin/env python
# webserver.py - a webserver which draws stats of sauspiel

import BaseHTTPServer
import matplotlib
import pylab
import io


class SauspielServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        path_list = path.split('?')
        if len(path_list)==1:
            self.send_error()
            return
        self.op = path_list[1]
        # dummy, op, arg1, arg2 = lst

        if self.op not in ('all', 'date', 'game'):
            self.send_error()
            return
        
        if self.op == 'game':
            if len(path_list)!=3:
                self.send_error()
                return
            self.game_count = int(path_list[2])

        # self.read_stats()
        buffer = self.draw_plot()

        self.send_response(200)
        self.send_header("Content-type", "image/png")
        self.end_headers()

        self.wfile.write(buffer.read())
        buffer.close()
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
        data_filename = "stats.txt"
        data = pylab.genfromtxt(data_filename , delimiter=',', dtype=int)
        y_data = data[:, 0]
        x_data = data[:, 1]
        if self.op == 'game':
            y_data = y_data[-self.game_count:]
            x_data = x_data[-self.game_count:]
        pylab.plot(x_data, y_data, '-')
        # pylab.show()
        buf = io.BytesIO()
        pylab.savefig(buf, format='png')
        buf.seek(0)
        # pylab.legend()
        # pylab.title("Title of Plot")
        # pylab.xlabel("X Axis Label")
        # pylab.ylabel("Y Axis Label")
        pylab.close()
        return buf

def run_server(port=9090):
    server_class = BaseHTTPServer.HTTPServer
    server_address = ('', port)
    handler_class = SauspielServer

    server = server_class(server_address, handler_class)
    server.serve_forever()

if __name__ == '__main__':
    run_server(port=50)
