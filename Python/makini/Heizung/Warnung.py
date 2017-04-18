#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import Klassen
import os


Kontrollintervall = 20 # in Sekunden
Stoerung= False
GPIO_EinAus = 4
Lampe = Klassen.Warnlampe(GPIO_EinAus)

while True:
	try:
		WarnText=""
		WarnDatei = open ("ErrorLog.txt","r")
		for line in WarnDatei.readlines():
			if line == "":
				break;
			else:
				WarnText+=line + "\n"#Email mit exception lines erstellen
				Stoerung = True
		
		#test ob alle programmteile Laufen
		#test ob die Dateien aktualisiert werden
		if Stoerung == True: 
			Kontrollintervall = 3600*3 #3 Stunden
			Lampe.An()#Alarmlampe an
			os.system("sudo python Mailsoftware.py " + "\"\"\"" + WarnText + "\"\"\"")#eMail versenden
		time.sleep(Kontrollintervall)
	
	except KeyboardInterrupt:
		exit()
