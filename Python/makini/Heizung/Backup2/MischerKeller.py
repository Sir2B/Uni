#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Klassen.py
import GPIO
import time

global SensornameZuTemperatur
global Parameter

def GetTemperaturen():
	global SensornameZuTemperatur
	SensornameZuTemperatur = pickle.load (open ("/home/pi/exchange/SensornameZuTemperatur","rb")) #Listeninhalt aktualisieren

def GetParameter():
	global Parameter
	Parameter = {}
	ParameterDatei = open("Parameter.txt","r")
	for zeile in ParameterDatei.readlines():
		Name,Wert = zeile.split("=")
		Parameter[Name]=Wert
	
def main(argv):
	global SensornameZuTemperatur
	global Parameter
	Mi = ref Mischer(GPIO_Oeffnen,GPIO_Schliessen)
	
	while True:
	try:
		GetTemperaturen()
		GetParameter() #Liest Parameter aus Datei ein !!!PARAMETERNAMEN NICHT VERÄNDERN!!!!!
		Mischer.Regeln(Parameter[Zyklenzeit], Parameter[TempZeitKoeff])
	except:
		print "Exception wurde ausgelöst"
		#EXCEPTION
		
		#WarnDatei einlesen und zusätzliche Fehler anhängen
		WarnDatei = open ("ErrorLog.txt","wr")
		for line in WarnDatei.readlines():
			Warnungen.append(line)
		Warnungen.append("Fehler in MischerKeller.py")
		WarnDatei.writelines(Warnungen)
		
		
		
		pass
	
	

if __name__ == "__main__":
    main(sys.argv)