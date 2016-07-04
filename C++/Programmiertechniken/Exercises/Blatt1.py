#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import time
import scipy.special


class HOSZ(object):
    def __init__(self):
        self.H = None
        self.datatype = complex

    def Matrix_HOSZ(self, N, L):
        delta_x = N/float(L)
        self.H = np.zeros((N, N), dtype=self.datatype)
        for n, y_row in enumerate(self.H):
            x = -L/2. + (n+1)*delta_x
            self.H[n][n] = 0.5*x*x + 1./(delta_x*delta_x)
            x_value = -1./(2*delta_x*delta_x)
            if n+1 < N:
                self.H[n][n+1] = x_value
            if n-1 > 0:
                self.H[n][n-1] = x_value

    def Eigensystem_HOSZ(self):
        w, v = np.linalg.eigh(self.H)
        return w, v

    def Analytische_Lsg_HOSZ(self, l):
        H_l = scipy.special.hermite(l)


def main():
    hosz = HOSZ()
    datatypes = [int, float, complex]
    for datatype in datatypes:
        t0 = time.clock()
        hosz.datatype = datatype
        hosz.Matrix_HOSZ(100, 10)
        hosz.Eigensystem_HOSZ()
        hosz.Analytische_Lsg_HOSZ(1)
        print("Time for {0}: {1}".format(datatype, time.clock()-t0))


if __name__ == "__main__":
    main()
