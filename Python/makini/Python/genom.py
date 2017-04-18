# -*- coding: utf-8 -*-
#!/usr/bin/env python


#finde die häufigsten wiederkehrenden Pattern der Länge M

import time

def Eingabe(): 
	M = raw_input("Die Länge eines Patterns: ")
	if not M.isdigit():
		print ("Des war a tobi")
		M = Eingabe()
	return int(M)

M = Eingabe()

begin = time.time()
file = open ("genom.txt")
zeilen = file.readlines()
genom = ""



for i in range (len(zeilen)):
	zeile = zeilen[i]
	genom += zeile
	
bst = []
val = []
mod = {}
moz = {}

for i in range (len(genom)-M):
	n = i+M
	if mod.has_key(genom[i:n]) == 1:
		mod[genom[i:n]] += 1
	else:
		mod[genom[i:n]] = 1
		bst.append(genom[i:n])
	
	

#bst.sort()

for key in bst:
	if not moz.has_key(mod[key]):
		moz[mod[key]] = key
		val.append(mod[key])

val.sort()
for i in range(len(val)): #nach bezeichnung sortiert
	print "%s : %.2f" %(moz[val[i]], val[i])

print "Dauer : %.2f s" % (time.time()-begin)
