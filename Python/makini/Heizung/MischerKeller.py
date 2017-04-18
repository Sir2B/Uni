#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Klassen
import RPi.GPIO as GPIO
import time
import sys
import cPickle as pickle
from Kommunikation import *

	
def main(argv):
	Parameter = GetParameter()
	Tag = True
	GPIO = GetGPIO("GPIO_raspi2")
	MischerKeller = Klassen.Mischer(GPIO[MischerWarm],GPIO[MischerKalt],"SensorTemperaturMischerKeller")
	
	while True:
		try:
			Parameter = GetParameter() #Liest Parameter aus Datei ein !!!PARAMETERNAMEN NICHT VERÄNDERN!!!!!
			MischerKeller.TemperaturAusgang = GetSensorTemperatur("SensorTemperaturMischerKeller")
			
			print "\nRegelt MischerKeller aufgrund folgender Werte:"
			print "Uhrzeit: %-20s " %time.strftime("%d.%m.%Y %H:%M:%S")
			print "AussenTemperatur: %-20s" %GetSensorTemperatur("SensorAussentemperatur")
			print "AusgangsTemperatur: %-20s" %MischerKeller.TemperaturAusgang
			print "TemperaturRaumSollTag: %-20s" %Parameter["TemperaturRaumSollTag"]
			print "TemperaturRaumSollNacht: %-20s" %Parameter["TemperaturRaumSollNacht"]
			print "AusgangsTemperaturSoll: %-20s" %MischerKeller.TemperaturAusgangSoll
			print "Zyklenzeit: %-20s" %Parameter["Zyklenzeit"]
			print "TempZeitKoeff: %-20s" %Parameter["TempZeitKoeff"]
			print "Es ist Tag: %-20s" %MischerKeller.Tag
			

			MischerKeller.Tageszeit(Parameter["TagBeginn"],Parameter["TagEnde"])
			MischerKeller.Regeln(Parameter["Zyklenzeit"], Parameter["TempZeitKoeff"])
		
		except KeyboardInterrupt:
			exit()
		except Exception as e:
			SchreibeFehler(e,"In MischerKeller.py ausgelöst")
			pass
		
	

if __name__ == "__main__":
    main(sys.argv)