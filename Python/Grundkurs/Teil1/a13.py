#!/usr/bin/env python
import time

#zahl=[ float(x) for x in open('numbers.dat').readlines() ]

f = open("numbers.dat")
zeilen = f.readlines()
zahl=[]
for line in zeilen:
	zahl.append(float(line))
f.close()

zahl.sort()
#print zahl
print "Kleinste Zahl = "+str(zahl[0])
print "Groesste Zahl = "+str(zahl[-1])


