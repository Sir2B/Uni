#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cPickle as pickle
import time
import os
	
def CompleteReset():
	try: 
		os.remove("DateipfadZuSensorname")
	except OSError:
		print "OSERROR DateipfadZuSensorname"
		pass
	try:	
		os.remove("SensornameZuTemperatur")
	except OSError:
		print "OSERROR SensornameZuTemperatur"
		pass		
	try:
		os.remove("SensornameZuFile")
	except OSError:
		print "OSERROR SensornameZuFile"
		pass
		
	print "\n\n!!!COMPLETE RESET!!!\n\n"
	
def PickleDictionaryOpener(Dateiname): #Öffnet Serialisiertes Dictionary aus Dateiname
	try:	
		Datei = pickle.load (open (Dateiname,"rb")) 
	except EOFError:		#falls gerade darauf zugegriffen wird
		time.sleep(.01)
		Datei = PickleDictionaryOpener(Dateiname)
	except IOError:		#falls Datei nicht vorhanden ist
		print "IOError"
		Datei = {}
		pass
	return Datei

def PickleDictionaryWriter(Dictionary,Dateiname): #Schreib Dictionary Serialisiert in Dateiname
	try:
		TempDictionary = pickle.load (open (Dateiname,"rb")) #Listeninhalt aktualisieren
	except IOError:
		TempDictionary = {}
	except EOFError:
		TempDictionary = {}
	for Key in TempDictionary.keys():
		try:
			Dictionary[Key]
		except KeyError:
			Dictionary[Key] = TempDictionary[Key]
	Datei = open(Dateiname,"wb")
	Datei.write ( pickle.dumps(Dictionary))
	Datei.close()	

def GetSensornameZuTemperatur():
	return PickleDictionaryOpener("SensornameZuTemperatur")

def GetSensorTemperatur(Sensorname):
	SensornameZuTemperatur = GetSensornameZuTemperatur()
	try:
		AktuelleTemperatur = SensornameZuTemperatur[Sensorname]
	except KeyError:
		AktuelleTemperatur ="SENSORNAME NICHT ANSPRECHBAR"
	return AktuelleTemperatur
	
def GetDateipfadZuSensorname():
	return PickleDictionaryOpener("DateipfadZuSensorname")
		
def GetSensornameZuFile():		
	return PickleDictionaryOpener("SensornameZuFile")
		
def GetParameter(): #Liest Parameter aus Textdatei ein !!!TEXTFORMATIERUNG BEACHTEN!!!
	Parameter = {}
	try:
		ParameterDatei = open("Parameter.txt","r")
		for zeile in ParameterDatei.readlines():
			zeile=zeile.replace("\n","")
			zeile=zeile.replace("\r","")
			Name,Wert = zeile.split("=")
			if Name == "TagEnde" or Name == "TagBeginn":
				Parameter[Name]=Wert
			else:
				Parameter[Name]=float(Wert)
		ParameterDatei.close()
	except ValueError:
		try:		
			zeile=zeile.replace("\n","")
			zeile=zeile.replace("\r","")
			Name,Wert = zeile.split("=")
			Parameter[Name]=Wert
			pass
		except ValueError:
			print "Inkonsistenz in Parameter.txt!!!"
			#time.sleep(1)
			#Parameter = GetParameter()
			pass
	return Parameter

def SensornameZuTemperatur2Datei(SensornameZuTemperatur): #Speichert SensornameZuTemperatur Serialisiert
	PickleDictionaryWriter(SensornameZuTemperatur,"SensornameZuTemperatur")
	
def DateipfadZuSensorname2Datei(DateipfadZuSensorname): #Speichert DateipfadZuSensorname Serialisiert
	PickleDictionaryWriter(DateipfadZuSensorname,"DateipfadZuSensorname")

def SensornameZuFile2Datei(SensornameZuFile): #Speichert SensornameZuFile Serialisiert
	PickleDictionaryWriter(SensornameZuFile,"SensornameZuFile")

def SchreibeFehler(Error, Programmteil):
	print repr(Error)," - in MischerKeller.py ausgelöst"
	#EXCEPTION
	#LAMPE ANSCHALTEN
	
	#WarnDatei einlesen und zusätzliche Fehler anhängen
	if not Programmteil:
		Programmteil = "Unbekannter Programmteil"
	Info = "Fehler in " + Programmteil
	Warnungen = [repr(Error) + Programmteil + "; Datum: " + str(time.strftime("%d.%m.%Y %H:%M:%S"))]
	try:
		WarnDatei = open ("ErrorLog.txt","wr")
		for line in WarnDatei.readlines():
			Warnungen.append(line)
		WarnDatei.writelines(Warnungen)
	except IOError: #falls Datei nicht forhanden
		WarnDatei = open ("ErrorLog.txt","w+")
		WarnDatei.writelines(Warnungen)

	pass