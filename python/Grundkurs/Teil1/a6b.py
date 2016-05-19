#!/usr/bin/env python

import math
import sys
import time

t1 = time.time()
#num = input()
num = int(sys.argv[1])
primes = []
i = 2

for zahl in range(2,num):
	wurzel = math.sqrt(zahl)
	i = 2
	while (i <= wurzel):
		if (zahl % i) == 0:
			#print "Keine Primzahl"
			break
		i+=1
	else:
		primes.append(zahl)

t2 = time.time()
print primes
print len(primes)
print "Zeit: " +str(t2-t1)
