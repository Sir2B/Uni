#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
# import sys
import time

# t1 = time.time()
# num = input()

# num = int(sys.argv[1])


def time_measure(func):
    def main(*args, **kwargs):
        start = time.time()
        erg = func(*args, **kwargs)
        print("{name} brauchte {zeit}".format(name=func.__name__, zeit=time.time()-start))
        return erg
    return main


def is_prim(number):
    wurzel = math.sqrt(number)
    if number < 2:
        return False
    i = 2
    while i <= wurzel:
        if (number % i) == 0:
            return False
        i += 1
    return True


@time_measure
def calc_primes(num):
    primes = []
    for zahl in range(2, num):
        if is_prim(zahl):
            primes.append(zahl)
    return primes


def main():
    num = 100000
    a = calc_primes(num)
    print("Es gibt {anzahl} Primzahlen, die kleiner sind als {zahl}".format(anzahl=num, zahl=len(a)))

if __name__ == "__main__":
    main()