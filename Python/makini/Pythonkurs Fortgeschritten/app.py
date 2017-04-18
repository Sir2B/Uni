__author__ = 'Tobias.Obermayer'

from klassen.klass1 import Klasse1
import cProfile
import re

def do_profiling(func):
    profiler = cProfile.Profile()
    try:
        profiler.enable()
        res = func()
        profiler.disable()
        return res
    finally:
        profiler.print_stats()


#
# def do_profiling(func):
#     def profiled_func(*args, **kwargs):
#         profiler = cProfile.Profile()
#         try:
#             profiler.enable()
#             res = func(*args, **kwargs)
#             profiler.disable()
#             return res
#         finally:
#             profiler.print_stats()
#
#     return profiled_func()


def tobi(func,n):
    def inner(*args,**kwargs):
        print 'hallo lustiger stinketobi'

    return inner()


def schleife(func,n):
    erg = None
    for i in range(n):
        erg = func()
    return erg


class Rechner:
    def __init__(self):
        pass

    @staticmethod

    def add(x, y):
        number_typen = (int, long, float, complex)
        if isinstance(x, number_typen) and isinstance(y, number_typen):
            return x+y
        else:
            raise ValueError

    def addklass1(self):
        self.klass1 = Klasse1()


def main():

    rech = Rechner()
    a = []

    for i in range(1000):
        for k in range(100):
            a.append(rech.add(i, k))


if __name__ == '__main__()':
    main()