# -*- coding: utf-8 -*-

import math
import numpy

AnzahlZufallszahlen = 1000


#fx = numpy.random.random(AnzahlZufallszahlen)
#fy = numpy.random.random(AnzahlZufallszahlen)
inner = .0
outer = .0
delta = 1.0

#for i in range(AnzahlZufallszahlen):
	#x = fx[i]
	#y = fy[i]
while delta >0.001:
	betrag = math.sqrt(numpy.random.random()**2+numpy.random.random()**2)
	if betrag <= 1:
		inner += 1
	elif betrag >1:
		outer += 1
	pi = (inner/AnzahlZufallszahlen)*4
	delta = math.sqrt((pi - math.pi)**2)*100


pi = (inner/AnzahlZufallszahlen)*4
print pi
print "Delta = " , math.sqrt((pi - math.pi)**2)*100
