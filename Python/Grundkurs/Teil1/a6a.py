#!/usr/bin/env python

import math
import sys

#zahl = input()
zahl = int(sys.argv[1])

i = 2
while (i <= math.sqrt(zahl)):
	if (zahl % i) == 0:
		print "Keine Primzahl"
		break
	i+=1
else:
	print "Primzahl"
