import numpy

data = numpy.loadtxt('rohr1.bin')

#print data
#b = numpy.fromfile('rohr1.bin', dtype=int)

#print b.mean(), b.std(), b.var()
print data.mean(), data.std()#, data.var()
