#!/usr/bin/env python
# -*- coding: utf-8 -*-

#To-Do list : Fehlerfunktion die beliebige fehler in datei schreibt


import time
import sys
#import os
import math
#import cPickle as pickle
from Kommunikation import *
global SensornameZuTemperatur
global SensornameZuFile
global DateipfadZuSensorname
global PathList
global NewPathList


def SingleRename(): #Umbenennung eines einzelnen Sensores
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	#Wähle Sensor zum löschen
	IDListe ={}
	ID = 0
	DateipfadZuSensorname = GetDateipfadZuSensorname()
	for Sensorpfad in DateipfadZuSensorname.keys():#Erstelle ID-Liste
		ID +=1
		IDListe[ID] = Sensorpfad
		#NamensListe[Sensorpfad] = i
		print ("%5i : %s") %(ID ,DateipfadZuSensorname[IDListe[ID]])
	
	while True:
		ID = raw_input("Auswahl: ") # Pfad -> Name
		try:
			ID=int(ID)
			RenamePath = IDListe[ID]
			break
		except KeyError:
			print "Spackooowoo! Den gibts nimmer !"
			pass
		except ValueError:
			print "Spackikuki!!! A ZAHL BITSCHEE!"
			pass
		except:
			print "Irgendetwas passt bei Benennung() nicht"
			pass


	SensorListe = open("Sensorliste.txt","r").readlines()
	IDListe ={}
	NamensListe = {}

	for i in range(len(SensorListe)): #Erstelle ID-Liste
		SensorListe[i] = SensorListe[i].replace("\n","")
		SensorListe[i] = SensorListe[i].replace("\r","")
		IDListe[i] = str(SensorListe[i])
		NamensListe[SensorListe[i]] = i

	for ID in IDListe:
		print ("%5i : %s") %(ID ,IDListe[ID])
	
	while True:
		ID = raw_input("Auswahl: ") # Pfad -> Name
		try:
			ID=int(ID)
			IDListe[ID]
			break
		except KeyError:
			print "Spackooowoo! Den gibts nimmer !"
			pass
		except ValueError:
			print "Spackikuki!!! A ZAHL BITSCHEE!"
			pass
		except:
			print "Irgendetwas passt bei Benennung() nicht"
			pass
	DateipfadZuSensorname[RenamePath] = IDListe[ID]
	del NamensListe[IDListe[ID]]
	del IDListe[ID]
	pass
	DateipfadZuSensorname2Datei(DateipfadZuSensorname)

def GetPath(): #Liest aktuelle Pfade und schreibt sie in NewPathList
	"Liest die Pfade aktueller Devices ein"
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	w1_master_slaves = open ("/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves").readlines() #liest SensorePfade ein
	NewPathList = [] #Pfadliste neu erstellen
	for line in w1_master_slaves:
		line=line.replace("\n","")
		#print line
		NewPathList.append("/sys/bus/w1/devices/" + line + "/w1_slave")
		

def GetFile(): #oeffne Temperaturdaten und Fuege Sie in SensornameZuFile ein
	"Öffnet Dateien und schreibt in Dictionary SensornameZuFile"
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	#SensornameZuFile = {}
	for i in PathList:
		try:
			SensornameZuFile[DateipfadZuSensorname[i]]=(open(i,"r"))  # Name -> Datei
		except KeyError:
			print "except"
			Benennung()
		

def Messung(): # Liest Temperatur aus geöffneten Daten aus
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	print "\n" 
	print "MESSUNG: "
	try:
		for Sensorname in DateipfadZuSensorname.values(): #Für jeden Sensor durchführen
			zeile=[]
			try:
				for line in SensornameZuFile[Sensorname]:
					zeile.append(line) #Zeilen aus Datei einlesen !!! DAUERT 0.8 SEKUNDEN pro Sensor!!!!
				if zeile[0].find("YES")!= (-1):#Teste ob Übertragung erfolgreich war
					SensornameZuFile[Sensorname].close()
					pos = zeile[1].find("t=")+2 # Startort des Temperaturwerts ermitteln
					Temperatur = float (zeile[1][pos:-1]) /1000 #Temperatur ermitteln
					SensornameZuTemperatur[Sensorname] = Temperatur
					SensornameZuTemperatur2Datei(SensornameZuTemperatur)
					print ("%30s : %-6.3f °C") %(Sensorname,Temperatur)
				else:
					SensornameZuTemperatur[Sensorname] = "TRANSMIT ERROR"
					print ("%30s : %-20s") %(Sensorname, SensornameZuTemperatur[Sensorname])
			except KeyError:
				SensornameZuTemperatur[Sensorname] = "NICHT VORHANDEN"
				print ("%30s : %-20s") %(Sensorname,SensornameZuTemperatur[Sensorname])
				pass
	except Exception, e:
		print repr(e), "in Messung"
			
	
def Benennung(): # Benennt neue Sensoren	

	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	GetPath()#NewPathList = GetPath()
	SensorListe = open("Sensorliste.txt","r").readlines()
	IDListe ={}
	NamensListe = {}
	for i in range(len(SensorListe)):
		SensorListe[i] = SensorListe[i].replace("\n","")
		SensorListe[i] = SensorListe[i].replace("\r","")
		IDListe[i] = str(SensorListe[i])
		NamensListe[SensorListe[i]] = i
	for i in NewPathList:
		try:
			DateipfadZuSensorname[i]	#Dictionary abtasten bis exception druch nichtvorhandenen Pfad ausgeloest wird
			del IDListe[NamensListe[DateipfadZuSensorname[i]]]
			del NamensListe[DateipfadZuSensorname[i]]
		except KeyError:
			print "Neuer Sensor verfügbar!"
			for ID in IDListe:
				print ("%5i : %s") %(ID ,IDListe[ID])
			
			while True:
				ID = raw_input("Auswahl: ") # Pfad -> Name
				
				try:
					ID=int(ID)
					IDListe[ID]
					break
				except KeyError:
					print "Spackooowoo! Den gibts nimmer !"
					pass
				except ValueError:
					print "Spackikuki!!! A ZAHL BITSCHEE!"
					pass
				except:
					print "Irgendetwas passt bei Benennung() nicht"
					pass
			DateipfadZuSensorname[i] = IDListe[ID]
			del NamensListe[IDListe[ID]]
			del IDListe[ID]
			pass
	DateipfadZuSensorname2Datei(DateipfadZuSensorname)
		

def Clean(): #Schmeisst entfernte Sensoren aus SensornameZuFile Raus
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	TempPathList = PathList
	GetPath()
	for i in NewPathList:
		TempPathList.remove(i)
	for i in TempPathList:
		del SensornameZuFile[DateipfadZuSensorname[i]]
	
			

def GetTemperaturen(): #Gesamter Vorgang zur Temperaturmessung
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	GetPath()#NewPathList = GetPath() #Liste mit Verzeichnissen zu den Temperaturdaten
	if len(NewPathList) > len(PathList):
		Benennung()
		PathList = NewPathList
	elif len(NewPathList) < len(PathList):
		Clean()
		PathList = NewPathList
	GetFile() #oeffne Temperaturdaten und Fuege Sie in SensornameZuFile ein
	Messung() #Name -> Temperatur
	#Temperatur2Datei(SensornameZuTemperatur)
		
	

def Initialisierung(argv): #öffnet Komm-Daten und erstellt bei bedarf neue
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	
	for params in argv:
		if params =="reset":
			CompleteReset()
		if params =="rename":
			SingleRename()
	
	SensornameZuTemperatur = {} # SensorName->Temperatur
	SensornameZuFile = {}	 # Name -> Datei
	DateipfadZuSensorname = {} # Pfad -> Name
	PathList = []  
	NewPathList = []
	DateipfadZuSensorname = GetDateipfadZuSensorname()
		


	
def main(argv):
	global SensornameZuTemperatur
	global SensornameZuFile
	global DateipfadZuSensorname
	global PathList
	global NewPathList
	Initialisierung(argv)
	while True:
		try:
			GetTemperaturen()
			#Messfehler()
			time.sleep(0.5)
			
		except IOError:
			print "IOERROR in main-Schleife"
			GetPath()
			PathList = NewPathList
			#DateipfadZuSensorname = {}
			pass
		except KeyboardInterrupt:
			exit()
		except Exception as e:
			SchreibeFehler(e,"In Temperaturmessung.py ausgelöst")
			pass
		
		
if __name__ == "__main__":
    main(sys.argv)