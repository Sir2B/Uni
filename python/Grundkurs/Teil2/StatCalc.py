import math
#
#   An object of class StatCalc can be used to compute several simple statistics
#   for a set of numbers.  Numbers are entered into the dataset using
#   the enter(double) method.  Methods are provided to return the following
#   statistics for the set of numbers that have been entered: The number
#   of items, the sum of the items, the average, and the standard deviation.
#

class StatCalc(object):

	def __init__(self):
		self.count = 0
		self.sum   = 0.
		self.squareSum   = 0.
		self.werte = []

	def enter(self, num):
		" Add the number to the dataset."
		self.count += 1
		self.sum += num
		self.squareSum += num*num
		self.werte.append(num)


	def getCount(self): 
		" Return number of items that have been entered."
		return self.count

	def getSum(self): 
		" Return the sum of all the items that have been entered."
		return self.sum

	def getMean(self): 
		" Return average of all the items that have been entered."
		return self.sum / self.count

	def getStandardDeviation(self): 
		" Return standard deviation of all the items that have been entered."
		return math.sqrt( self.squareSum/self.count - self.getMean()**2 )

	def getMin(self):
		" blablablabl. "
		a = self.werte
		a.sort()
		return a[0]

	def getMax(self):
		" blablablabl. "
		a = self.werte
		a.sort()
		return a[-1]	
   
# end of class StatCalc
