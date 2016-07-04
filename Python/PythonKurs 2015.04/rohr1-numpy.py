import numpy

data = numpy.loadtxt('rohr1.dat')
print len(data)
print numpy.min(data)
print numpy.max(data)

counter = 0
for number in data:
	if number < -50:
		counter += 1
print counter
print numpy.median(data)
