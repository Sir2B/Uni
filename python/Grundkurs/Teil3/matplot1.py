#!/usr/bin/env python

from pylab import *

if __name__ == '__main__':

    # read in data to list
    data = loadtxt('numbers.dat')
    # create x data
    x = range(0,len(data))
    # create empty figure
    figure(1,figsize=(6,4))
    xlabel('x')
    ylabel('numbers')
    # plot data with data points
    plot(x,data,'.')
    title('Content of numbers.dat')
    # save figure to PNG file
    savefig('numbers.png',dpi=72)
    # show canvas
    show()
