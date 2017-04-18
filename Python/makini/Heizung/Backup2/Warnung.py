#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import Klassen.py


Kontrollintervall = 20 # in Sekunden
Stoerung= False
Lampe = ref Warnlampe()

while True:
	try:
		WarnDatei = open ("ErrorLog.txt","r")
		for line in WarnDatei.readlines():
			if line == "":
				break;
			#Email mit exception lines erstellen
		#test ob alle programmteile Laufen
		#test ob die Dateien aktualisiert werden
		if Stoerung = True: 
			Kontrollintervall = 3600*3 #3 Stunden
			Lampe.An())#Alarmlampe an
			#eMail versenden
		time.sleep(Kontrollintervall)
	except:
		pass
