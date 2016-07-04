#!/usr/bin/env python

from matplotlib import pyplot as plt
from sys import argv, exit, stderr
import numpy as np

if __name__ == "__main__":
    
    try:
        data = np.loadtxt(argv[1])
    except IndexError:
        stderr.write("USAGE: input_file")
        exit(1)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xscale('log')
    ax.set_yscale('log')

    try:
        ax.plot(data[:,0], data[:,1], label="rect")
        ax.plot(data[:,0], data[:,2], label="trap")
        ax.plot(data[:,0], data[:,3], label="simp")
    except ValueError:
        stderr.write("Some y-values are 0. Plotting y + 1 instead.\n")
        ax.plot(data[:,0], data[:,1]+1, label="rect")
        ax.plot(data[:,0], data[:,2]+1, label="trap")
        ax.plot(data[:,0], data[:,3]+1, label="simp")


    plt.legend()
    plt.show()

    exit(0)
