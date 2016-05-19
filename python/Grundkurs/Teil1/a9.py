#!/usr/bin/env python

import sys

num = int(sys.argv[1])

def fak (n):
	e = 1
	for zahl in range(2,n+1):
		e *= zahl
	return e


print str(num)+ "! = "+ str(fak(num))
