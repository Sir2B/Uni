__author__ = 'Tobias.Obermayer'

def tobiRator():
    for i in xrange(100000000):
        yield 'tobi ist dumm hoch {zahl}'.format(zahl=i)




print 'start'
a = tobiRator()
while True:
    print a.next()
