from Kommunikation import *
from Klassen import *
import RPi.GPIO as GPIO







def main():
		
	###INITIALISIERUNG###
	GPIOPins = GetGPIO()
	Parameter = GetParameter()
	
	Volumen= 2000 #in Liter
	Entladepumpe= GPIOPins ["EntladepumpePufferHeizraum"] #Namen müssen noch abgeglichen werden
	Beladepumpe = GPIOPins ["BeladepumpePufferHeizraum"]
	PufferHeizraum = Puffer(Volumen,Entladepumpe,Beladepumpe,"Heizraum")
	
	while True: #MainSchleife
		KontrollePufferHeizraum(PufferHeizraum)





if name == "__main__":
	main()