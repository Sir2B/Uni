# finde Primzahlen von pmin bis pmax
#
# Aufruf 
# findprimes [pmin] [nrange] [index]
#
import sys


try:
    pmin = int(sys.argv[1])
    nrange = int(sys.argv[2])
except:
    print "No range given"
    pmin=3
    nrange = 12000000


try:
    index = int(sys.argv[3])
except:    
    index = 0

pmin += index * nrange
pmax = pmin + nrange

primemax = 100000

if primemax*primemax < pmax:
    print "Max prime :", primemax*primemax
    pmax = primemax*primemax

# pmin odd
if pmin%2 == 0:
    pmin +=1


print "Finding primes from ", pmin, " to ", pmax



# get ref list
primeliste = [2, 3, 5, 7 ]
p = 11
while p < primemax:

    for t in primeliste:
        if p % t == 0 :
            break
      
        if t*t > p : # reached limit, must be prime
            primeliste.append(p)
            break
        #
    #
    p += 2



# primes in specified range
primeres = []
p = pmin
while p < pmax:
    for t in primeliste:
        if p % t == 0 :
            break
      
        if t*t > p : # reached limit, must be prime
            primeres.append(p)
            break
        #
    p += 2

print len(primeres)
print primeres[-10:]

# store
import numpy
outf="primes_%d_%d.dat" % (pmin, pmax)
a=numpy.array(primeres)
a.tofile(outf)
