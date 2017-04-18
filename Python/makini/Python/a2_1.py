#!/usr/bin/env python

import math
import random
from StatCalc import StatCalc

#
#   An object of class StatCalc can be used to compute several simple statistics
#   for a set of numbers.  Numbers are entered into the dataset using
#   the enter(double) method.  Methods are provided to return the following
#   statistics for the set of numbers that have been entered: The number
#   of items, the sum of the items, the average, and the standard deviation.
#

   
# end of class StatCalc



stat = StatCalc()
for i in range(00):
	a = (random.random())
	#print "%5.3f" % (a)
	stat.enter(a)
try:
	print "Der Durchschnittswert ist: %6.5f" % stat.getMean()
	print "Die Standardabweichung ist: %6.5f" % stat.getStandardDeviation()

except:
	print "Der Durchschnittswert ist: ", stat.getMean()
	print "Die Standardabweichung ist: ", stat.getStandardDeviation()

try:
	print "Minimum: %6.4f" % stat.getMinimum()
	print "Maximum: %6.4f" % stat.getMaximum()
	
except:
	print "Minimum: ", stat.getMinimum()
	print "Maximum: ", stat.getMaximum()
