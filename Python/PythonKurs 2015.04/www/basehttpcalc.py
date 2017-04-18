#!/usr/bin/env python
# basehttpcalc.py -- a basic HTTP server / calculator

import BaseHTTPServer

class CalcHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path

        lst = path.split('/')
        if len(lst) != 4:
            self.send_response(403)
            self.end_headers()
            self.wfile.write('Illegal syntax. '
                             'Use /{add,sub,mul,div}/num1/num2'
                             '\r\n')
            return
        
        dummy, op, arg1, arg2 = lst

        if op not in ('add', 'sub', 'mul', 'div'):
            self.send_response(403)
            self.end_headers()
            self.wfile.write('Illegal operation: ' + op + '\r\n')
            return
        
        try:
            numarg1 = float(arg1)
            numarg2 = float(arg2)
        except ValueError:
            self.send_response(403)
            self.end_headers()
            self.wfile.write('Numerical arguments expected' + '\r\n')
            return

        if op == 'add': result = numarg1 + numarg2
        elif op == 'sub': result = numarg1 - numarg2
        elif op == 'mul': result = numarg1 * numarg2
        elif op == 'div':
            if numarg2 == 0: result = 'NaN'
            else:            result = numarg1 / numarg2
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(result) + '\r\n')
            
def run_server(port=9090):
    server_class   = BaseHTTPServer.HTTPServer
    server_address = ('', port)
    handler_class  = CalcHandler
    
    server = server_class(server_address, handler_class)
    server.serve_forever()

if __name__ == '__main__':
    run_server()
