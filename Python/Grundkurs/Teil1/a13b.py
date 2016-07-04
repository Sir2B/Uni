#!/usr/bin/env python

import sys
num = float(sys.argv[1])

f = open("numbers.dat")
Zeile = f.readlines()
for i in range(0,len(Zeile)):
	Zeile[i] = float(Zeile[i])


def dif(a,b):
	x= a - b
	if x >= 0: return x
	else: return -x

Zahl = Zeile[0]
abstand = dif(num,Zeile[0])

for i in range(1,len(Zeile)):
	if (dif(num, Zeile[i]) < abstand):
	   abstand = dif(num, Zeile[i])
	   Zahl = Zeile[i]

#print num
print Zeile
print Zahl
#print dif(4,-2)

f.close()
