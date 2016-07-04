#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Tobias'

import time
import numpy as np
import operator

laenge = 1000000
a = np.arange(laenge)
b = np.arange(laenge)

t1 = time.time()
c = a + b
print("Mit numpy:", time.time()-t1)

t1 = time.time()
d = [x+y for x, y in zip(a, b)]
print("Mit list comprehension und zip:", time.time()-t1)

t1 = time.time()
e = [a[i]+b[i] for i in range(len(a))]
print("Mit list comprehension ohne zip:", time.time()-t1)

t1 = time.time()
map(operator.add, a, b)
print("Mit operator add:", time.time()-t1)

t1 = time.time()
f = []
for i in range(len(a)):
    f.append(a[i] + b[i])
print("Mit for-Schleife:", time.time()-t1)

if not (list(c) == d == e == f):
    print("Fehler")