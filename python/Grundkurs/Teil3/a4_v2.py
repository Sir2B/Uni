# -*- coding: utf-8 -*-
import operator
import time
import collections

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
#DNAdic = {}
DNAList = []
#~ global DNACounter


for i in range(0,(len(DNA)-Laenge)):
	seq = DNA[i:i+Laenge]
	#DNACounter.update([seq])
	DNAList.append(seq)
	
DNACounter = collections.Counter(DNAList)

print DNACounter.most_common(1)
print "Dauer %1.3f" %(time.time()-t1)
