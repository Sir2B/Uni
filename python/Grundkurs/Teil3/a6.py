# -*- coding: utf-8 -*-
import random
import math
import numpy
import time


t1= time.time()
gesamt = 1000000
zaehler = 0
#px = []
#py = []
for i in range(gesamt):
	#px.append(random.random())
	#py.append(random.random())
	if (random.random()**2+random.random()**2)< 1:
		zaehler += 1
mypi1= float(zaehler)/gesamt*4
t2= time.time()



zaehler = 0

for i in range(gesamt):
	if (numpy.random.random()**2+numpy.random.random()**2)< 1:
		zaehler += 1

mypi2= float(zaehler)/gesamt*4

t3= time.time()



px = numpy.random.random(gesamt)
py = numpy.random.random(gesamt)
r = px*px + py*py
mypi3 = float(len(numpy.where(r<1)[0]))/len(r)*4
t4= time.time()



print "Pi    = %9.8f" %math.pi
print "MyPi1 = %9.8f" %(mypi1)
print "MyPi2 = %9.8f" %(mypi2)
print "MyPi3 = %9.8f" %(mypi3)
print "Delta = %9.8f%%" %(abs(mypi1-math.pi)*100)
print "Zeit1: %6.2f Sekunden" %(t2-t1)
print "Zeit2: %6.2f Sekunden" %(t3-t2)
print "Zeit3: %6.2f Sekunden" %(t4-t3)
