
f = open("kant.txt")
f2 = open("kant_gross.txt","w")
Zeilen = f.readlines()
counter = 0
print "Anzahl Zeilen: " + str(len(Zeilen))
for i in range(0,len(Zeilen)):
	f2.write(Zeilen[i].upper())
	counter += Zeilen[i].count("Vernunft")

print "Anzahl 'Vernunft': "+str(counter)
f.close()
f2.close()

