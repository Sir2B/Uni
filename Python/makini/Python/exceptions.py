
import math

file = open ("vorwahl.txt")
plz={}
nummer = 0
ort = ""
#Create List
while  file.readline() <> "":
    line = file.readline()
    #leerzeichen = line.find(" ")
    nummer, ort = line.split(" ",1)
    print nummer
    print ort
    plz[nummer]=ort
   
print "plz eingeben: "
zahl = input()

print plz[zahl]