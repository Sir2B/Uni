# -*- coding: utf-8 -*-
import codecs

f = codecs.open("vorwahl.txt", "r", "iso-8859-15")
#f = open("vorwahl.txt")
zeilen = f.readlines()
print 'Zahl der Zeilen', len(zeilen)

vwort = {}
for zeile in zeilen:
	vorw,ort = zeile.split(" ",1)
	if vwort.has_key(vorw):
		vwort[vorw] += ", " +ort #wenn mehrere Orte selbe Vorwahls
	else:
		vwort[vorw] = ort


while(True):
	try:
		auswahl = int(raw_input("Vorwahl (0) oder Ort (1)?"))
		if auswahl == 0 or auswahl == 1:
			print 'Bitte 0 oder 1 eingeben'
			break
	except:
		print 'Bitte 0 oder 1 eingeben'

if auswahl == 0: #Vorwahl-Suche
	suche_vorw = raw_input("Vorwahl eingeben: ")
	try:
		print vwort[suche_vorw]
	except:
		print "Vorwahl nicht vorhanden"
else:#Orts-Suche
	found = False
	suche_ort = raw_inpzut("Ort eingeben: ")
	suche_ort = suche_ort.decode("utf-8")
	for (vorw,ort) in vwort.items():
		if ort.find(suche_ort) >= 0:
			print vorw, ort
			found = True
	if not found:
		print 'Ort nicht gefunden: ', suche_ort, type(suche_ort)
