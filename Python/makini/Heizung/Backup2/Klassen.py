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
		#Ladezustand ermitteln
	def EntladepumpeEin(self):
		#Entladepumpe einschalten
	def EntladepumpeAus(self):
		#Entladepumpe ausschalten
	def EntladepumpeBlockieren(self):
		#Entladepumpe ausschalten		
	def BeladepumpeEin(self):
		#Entladepumpe einschalten
	def BeladepumpeAus(self):
		#Entladepumpe ausschalten
	def BeladepumpeBlockieren(self):
		#Entladepumpe ausschalten	
		
class Pumpe:
	Blockiert
	IstEinAus
	def Ein(self):
		#GPIO Pin einschalten
	def Aus(self):
		#GPIO Pin ausschalten
		
class Ventil:
	IstAufZu
	def Auf():
		#GPIO Pin zu aufmachen
	def Zu():
		
class Mischer:
	def __init__(self,RelaiOeffnen,RelaiSchliessen)
		self.TemperaturAusgang
		self.TemperaturAusgangSoll
		self.IstAktiv = False
		self.SchalterOeffnen  = RelaiOeffnen
		self.SchalterSchliessen = RelaiSchliessen
	def Regeln(self,Zyklenzeit, TempZeitKoeff):
		
		if TemperaturAusgang > TemperaturAusgangSoll:
			DeltaT = TemperaturAusgang - TemperaturAusgangSoll
		elif TemperaturAusgang < TemperaturAusgangSoll:	
			DeltaT = TemperaturAusgangSoll - TemperaturAusgang
		
		EinschaltAnteil = (DeltaT * TempZeitKoeff)/100 #Prozentualer Anteiler am Zyklus in der der Mischer öffnet
		if EinschaltAnteil > 1:
			EinschaltAnteil = 1
		if EinschaltAnteil < 0.001:
			EinschaltAnteil = 0
		EinschaltDauer = EinschaltAnteil*Zyklenzeit # Absolute Öffnungsdauer
		PausenDauer = Zyklenzeit*(1-EinschaltAnteil) # Wartezeit
		
		if TemperaturAusgang > TemperaturAusgangSoll:
			Schliessen (EinschaltDauer,PausenDauer)
		elif TemperaturAusgang < TemperaturAusgangSoll:	
			Oeffnen (EinschaltDauer,PausenDauer)
			
	def Oeffnen(self,EinschaltAnteil, PausenDauer):
		SchalterSchliessen = 0
		SchalterOeffnen = 1
		time.sleep ( EinschaltAnteil )
		SchalterOeffnen = 0
		
	def Schliessen(self,EinschaltAnteil, PausenDauer):
		SchalterOeffnen = 0
		SchalterSchliessen = 1
		time.sleep ( EinschaltAnteil )
		SchalterSchliessen = 0		
	
class Warnlampe:
	def __init__(self,Pin)
		self.GPIO_Pin = Pin

	def An():
		GPIO_Pin = 1
	def Aus():
		GPIO_Pin = 0
