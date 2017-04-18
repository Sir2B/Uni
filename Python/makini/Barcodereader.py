#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from sys import stdin
import sys

import os
from DatenbankDummy import *
import DatenbankDummy

global TimeForInput
TimeForInput = 2.3

DatenBank = DatenbankDummy._DatenBank()

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
	screen."""
    def __init__(self):
        try:
            import msvcrt
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getwch()


getch = _Getch()

def BarcodeRead():
	global TimeForInput
	print ("BarcodeRead...")
	Input = ""
	InputChar = str(getch.impl())
	if InputChar =='':
		exit()
	#time.sleep(.5)
	if InputChar != "":
		start = time.time()
		while time.time()-start < TimeForInput : #1 Sekunde Zeit für eingabe
			Input = Input + InputChar
			print (InputChar)
			InputChar = str(getch.impl()) #hier wird noch ein break von nöten sein
			if InputChar =='':
				exit()
			print (time.time()-start)
	return Input
	
	
def BarcodeOut(Barcode):	
	print ("BarcodeOut...")
	Output = open("output.txt","w+")
	Output.write(Barcode)
	Output.close()
	DatenBank.ReadUser(Barcode) #Testen ob UserID vorhanden ist und anschliessend schreiben von Daten
	DatenBank.WriteDate(Barcode,time.time())
	
def Initialisierung(argv):
	global TimeForInput
	for arg in argv:
		if arg == '-time' or arg == '-timeforinput':
			try:
				NewTimeForInput = float(argv[argv(arg)+1])
				print ("TimeForInput: %f" %NewTimeForInput)
				TimeForInput = NewTimeForInput
			except IndexError:
				print ("TimeForInput: %f" %TimeForInput)
			except ValueError:
				print ("TimeForInput-Argument erfordert eine Zahl")
	
			
def main (argv):
	Initialisierung(argv)
	# 1. Auf BarcodeRead warten
	try:
		while True:
		
			BarcodeOut(BarcodeRead())
		#BarcodeRead(Input)
	except KeyboardInterrupt:
		exit()
	# 2. Barcode überprüfunden an Dummy Datenbank
	
	# 3. Barcode in Datei ausgeben



if __name__ == "__main__":
	main(sys.argv)


