__author__ = 'Tobias.Obermayer'

import numpy
import numpy.random
from numpy.core import *

def calcPi(iterations):

    if __name__ == "__main__" :
        num = iterations
        rx = numpy.random.random(num)
        ry = numpy.random.random(num)
        r = numpy.sqrt(rx**2 + ry**2)
        print float(len(where(r<1)[0]))/len(r)
        print pi/4


def main():
    calcPi(10000)

if __name__ == '__main__':
    main()