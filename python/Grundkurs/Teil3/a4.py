# -*- coding: utf-8 -*-
import operator
import time

f= open("genom.txt")
Zeilen= f.readlines()
#global Laenge
DNA = ""
def Abfrage():
	Laenge = raw_input('Bitte Zahl eingeben: ')
	if not Laenge.isdigit():
		print "Eine Zahl eingeben!"
		Laenge = Abfrage()
	return int(Laenge)
	
Laenge = Abfrage()

t1 = time.time()
for i in range(len(Zeilen)):
	DNA += Zeilen[i][:-2]

#print DNA
DNAdic = {}

for i in range(0,(len(DNA)-Laenge)):
	seq = DNA[i:i+Laenge]
	if not DNAdic.has_key(seq):
		DNAdic[seq]=1
	else:
		DNAdic[seq]+=1


#print DNAdic
#for key in sorted(DNAdic.keys()):
#    print "%s: %s" % (key, DNAdic[key])

DNAdic_sorted =  sorted(DNAdic.items(), key=operator.itemgetter(1))
#print "%s: %s" %(DNAdic_sorted[0][0], DNAdic_sorted[0][1])

#print len(DNAdic_sorted)
#print DNAdic_sorted
anzahl_rueckgabe = 3
#for i in range(0,(len(DNAdic_sorted))): # komplett
	#s1 = DNAdic_sorted[i][0]
	#s2 = DNAdic_sorted[i][1]
	#~ print "%s: %s" % (DNAdic_sorted[i])

print "%s: %s" % (DNAdic_sorted[-1:][0])
print "Dauer: %4.3f" %(time.time()-t1)
