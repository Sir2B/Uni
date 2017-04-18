try:

    from SocketServer import TCPServer, StreamRequestHandler

    class EchoHandler(StreamRequestHandler):
        def handle(self):

            print "Serving client:", self.client_address
            #addOperation = '+'
            for line in (self.rfile):
                #if addOperation in line:
                 #   a, b = line.split(addOperation)
                try:
                    self.wfile.write(str(eval(line)))#str(Add(a,b)))
                except Exception as e:
                    print e


    def Add(*args):
        erg = 0
        for x in args:
            erg += eval(args)
        return erg

    TCPServer.allow_reuse_address = True
    srv = TCPServer(('', 7070), EchoHandler)

    srv.serve_forever()
except KeyboardInterrupt:
    exit()