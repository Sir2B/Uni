#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
class Puffer:
	def __init__(self,vol,EntlPumpe,LadePumpe):	
		self.Volumen 
		self.Entladepumpe
		self.Beladepumpe
		self.Temperatur1
		self.Temperatur2
		self.Temperatur3
		self.Temperatur4
		self.Temperatur5
		self.Temperatur6
		self.Ladezustand
		
	def ErmittleLadezustand():
		i=1#Ladezustand ermitteln
	def EntladepumpeEin(self):
		i=1#Entladepumpe einschalten
	def EntladepumpeAus(self):
		i=1#Entladepumpe ausschalten
	def EntladepumpeBlockieren(self):
		i=1#Entladepumpe ausschalten		
	def BeladepumpeEin(self):
		i=1#Entladepumpe einschalten
	def BeladepumpeAus(self):
		i=1#Entladepumpe ausschalten
	def BeladepumpeBlockieren(self):
		i=1#Entladepumpe ausschalten	
		
class Pumpe:
	def __init__(self,GPIO_EinAus):
		self.GPIO_EinAus = GPIO_EinAus
		self.Blockiert
		self.IstEinAus
	def Ein(self):	#GPIO Pin einschalten
		GPIO_EinAus=1
	def Aus(self):	#GPIO Pin ausschalten
		GPIO_EinAus=0
		
class Ventil:
	def __init__(self,GPIO_Auf,GPIO_Zu):	
		self.IstAufZu
		self.GPIO_Auf = GPIO_Auf
		self.GPIO_Zu = GPIO_Zu
	def Auf(self): #Ventil Öffnen
		GPIO_Zu = 0
		GPIO_Auf =1
	def Zu(self): #Ventil Schliessen
		GPIO_Auf =0
		GPIO_Zu = 1

		
class Mischer:
	def __init__(self,RelaiOeffnen,RelaiSchliessen,SensorTemperaturMischer):
		self.SensorTemperaturMischer = SensorTemperaturMischer
		self.TemperaturAusgang = 0 #°C
		self.TemperaturAusgangSoll = 0 # °C
		self.IstAktiv = True
		self.Tag = True
		self.SchalterOeffnen  = RelaiOeffnen
		self.SchalterSchliessen = RelaiSchliessen
	
	def Regeln(self,Zyklenzeit, TempZeitKoeff):
		self.GetSollTemperatur()
		if self.TemperaturAusgang > self.TemperaturAusgangSoll:
			DeltaT = self.TemperaturAusgang - self.TemperaturAusgangSoll
		elif self.TemperaturAusgang < self.TemperaturAusgangSoll:	
			DeltaT = self.TemperaturAusgangSoll - self.TemperaturAusgang
		else:
			DeltaT =0
			time.sleep(Zyklenzeit)
		EinschaltAnteil = (DeltaT * float(TempZeitKoeff))/100 #Prozentualer Anteiler am Zyklus in der der Mischer öffnet
		if EinschaltAnteil > 1:
			EinschaltAnteil = 1
		if EinschaltAnteil < 0.001:
			EinschaltAnteil = 0
		EinschaltDauer = EinschaltAnteil*Zyklenzeit # Absolute Öffnungsdauer
		PausenDauer = Zyklenzeit*(1-EinschaltAnteil) # Wartezeit
		
		if self.TemperaturAusgang > self.TemperaturAusgangSoll:
			self.Schliessen (EinschaltDauer,PausenDauer)
		elif self.TemperaturAusgang < self.TemperaturAusgangSoll:	
			self.Oeffnen (EinschaltDauer,PausenDauer)
	
	def hmTimeValidate(self,gettime):
		try:
			h,m = gettime.split(":")
			if len(h)==1: #Schau ob die Zeit richtig formatiert ist
				h = "0" + h
			if len(h)==0: #Schau ob die Zeit richtig formatiert ist
				h = "00"
			if len(m)==1: #Schau ob die Zeit richtig formatiert ist
				m = m +"0"			
			if len(m)==0: #Schau ob die Zeit richtig formatiert ist
				m = "00"
			if int(m) > 60:
				m = str(int(m)-60)
				h = str(int(h)+1)
			elif int(m)<0:
				m="00"
			if int(h) > 24:
				h = str(int(h)-24)
			elif int(h)<0:
				h="00"
			gettime = h + ":" + m
			return gettime
		except ValueError:
			gettime = gettime + ":00"
			return gettime
		
		
			
	def Tageszeit (self,TagBeginn,TagEnde):
		TagBeginn = str(TagBeginn)
		TagEnde = str(TagEnde)
		TagBeginn=self.hmTimeValidate(TagBeginn)
		TagEnde = self.hmTimeValidate(TagEnde)
			
			
		stunde = (time.strftime("%H:%M"))
		try:
			if TagBeginn > TagEnde: #Falls Tagessprung zwischen beginn und ende
				if stunde > TagBeginn or stunde < TagEnde: #Falls nach Tagesstart oder vor Tagesende
					self.Tag = True
				else:
					self.Tag = False
			elif TagBeginn < TagEnde:
				if stunde > TagBeginn and stunde < TagEnde:
					self.Tag = True
				else:
					self.Tag = False
			else:
				print "in Parameterliste: TagBeginn = TagEnde !! "
				self.Tag = True
		except KeyboardInterrupt:
			pass
		except ValueError:
			SchreibeFehler("ValueError", " in TagesZeit")
			
	def GetSollTemperatur(self):
		from Kommunikation import *
		import math
		Parameter = GetParameter()
		tempaussen = GetSensorTemperatur("SensorAussentemperatur")
		if isinstance(tempaussen, basestring):
			print "\nSensorstatus:" ,tempaussen 
			if Parameter["HeizungVorlaufTemperaturSollNotfall"]:
				self.TemperaturAusgangSoll = Parameter["HeizungVorlaufTemperaturSollNotfall"]
			else:
				self.TemperaturAusgangSoll = 50
			return 
		steigung = Parameter["HeizungVorlaufSollSteigung"]
		if self.Tag:
			tempinnensoll = Parameter["TemperaturRaumSollTag"]
		else:
			tempinnensoll = Parameter["TemperaturRaumSollNacht"]
		DeltaT = tempinnensoll - tempaussen
		DeltaTStart = 0.5
		if	DeltaT<= DeltaTStart:
			self.IstAktiv = False #Pumpe ausschalten
			self.TemperaturAusgangSoll = tempinnensoll
		elif DeltaT > DeltaTStart:
			self.IstAktiv = True #Pumpe ausschalten
			self.TemperaturAusgangSoll = steigung*math.sqrt(DeltaT) +tempinnensoll+1
			if self.TemperaturAusgangSoll > 85: # Begrenzung
				self.TemperaturAusgangSoll = 85
	
	def Oeffnen(self,EinschaltAnteil, PausenDauer):
		if self.IstAktiv == False:
			print "Mischer Inaktiv"
			time.sleep(.5)
			return
		print "Mischer Öffnet"
		SchalterSchliessen = 0
		SchalterOeffnen = 1
		time.sleep ( EinschaltAnteil )
		SchalterOeffnen = 0
		time.sleep ( PausenDauer )
		
	def Schliessen(self,EinschaltAnteil, PausenDauer):
		if self.IstAktiv == False:
			print "Mischer Inaktiv"
			time.sleep(1)
			return
		print "Mischer Schliesst"		
		SchalterOeffnen = 0
		SchalterSchliessen = 1
		time.sleep ( EinschaltAnteil )
		SchalterSchliessen = 0		
		time.sleep ( PausenDauer )	
	
class Warnlampe:
	def __init__(self,GPIO_EinAus):
		self.GPIO_Pin = GPIO_EinAus

	def An(self):
		GPIO_Pin = 1
	def Aus(self):
		GPIO_Pin = 0
