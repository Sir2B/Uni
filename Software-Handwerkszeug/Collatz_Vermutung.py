#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pylab as pl
N=[]
Count=[]
for n in range(1,10000):
	N.append(n)
	#n = input('Geben sie eine Zahl ein: ')
	count = 0
	while (n != 1):
		
		if (n%2 == 0):
			n /= 2
		else:
			n = 3*n +1
		#print n
		count += 1
	Count.append(count)
	#print N, count


pl.plot(N,Count,'.')
pl.savefig('plot.png',dpi=72)
pl.show()
