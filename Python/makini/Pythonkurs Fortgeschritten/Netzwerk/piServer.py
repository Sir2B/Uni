__author__ = 'Tobias.Obermayer'
import numpy
import numpy.random
from numpy.core import *
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn

def calcPi(iterations):
    num = iterations
    rx = numpy.random.random(num)
    ry = numpy.random.random(num)
    r = numpy.sqrt(rx**2 + ry**2)
    return 4*float(len(where(r < 1)[0]))/len(r)

class ThreadedSimpleXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer): pass

def main():
    server = ThreadedSimpleXMLRPCServer(('', 7071), allow_none=True)
    server.register_introspection_functions()
    server.register_function(calcPi, 'calcPi')

    server.serve_forever()

if __name__ == '__main__':
    main()