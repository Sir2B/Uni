import sys

datei1 = sys.argv[1]
datei2 = sys.argv[2]
f1 = open(datei1)
f2 = open(datei2, "w")
Zeile = f1.readlines()
for i in range(0,len(Zeile)):
	f2.write(Zeile[i])

f1.close()
f2.close()
