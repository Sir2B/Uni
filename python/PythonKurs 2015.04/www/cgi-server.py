import BaseHTTPServer
import CGIHTTPServer
            
def run_server(port=9070):
    server_class   = BaseHTTPServer.HTTPServer
    handler_class  = CGIHTTPServer.CGIHTTPRequestHandler
    handler_class.cgi_directories = ['/cgi-bin']
    server_address = ('', port)
    
    server = server_class(server_address, handler_class)
    server.serve_forever()

if __name__ == '__main__':
    run_server()
