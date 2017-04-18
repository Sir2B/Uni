# -*- coding: utf-8 -*-

import math
import curses
import time
from curses import wrapper


stdscr = curses.initscr()
curses.noecho()
curses.numpad()
curses.cbreak()



class Lander(object):
	def __init__ (self, m = 1, t = 0, h = 0):
		self.Leermasse = m
		self.Treibstoff = t
		self.Hoehe = h
		self.Speed = 0
		self.Gas = 0
		self.key = "0"

	def Schritt (self, zeit,g):
		beschl = self.Gas
		a = g - beschl
		self.Speed += a*zeit
		self.Masse = self.Treibstoff+self.Leermasse
		self.Hoehe = self.Hoehe - self.Speed*zeit - 0.5*g*zeit
		if self.Hoehe < 0:
			self.Hoehe = 0
		self.Treibstoff = self.Treibstoff-self.Gas
		begin = time.time()
		self.key = "-1"
		time.sleep(zeit)
		#stdscr.clear()
		stdscr.refresh()
		print "Gas: %6.0f " % self.Gas ,"  Hoehe: %6.1f " % self.Hoehe ,"  Speed: %6.1f " %self.Speed , stdscr.getch()
		
		
tobi = Lander (1000,100,1000000)
quantisierung = 0.2
g = 5.2

begin_x = 20; begin_y = 7
height = 5; width = 40
win = curses.newwin(height, width, begin_y, begin_x)

stdscr = win

while True: #tobi.Hoehe > 0:
	try:    
		tobi.Schritt (quantisierung,g)
		print tobi.key
		if curses.KEY_UP == stdscr.nodelay(1):
			if tobi.Gas >= 100:
				tobi.Gas = 100
			elif tobi.Gas < 100:
				tobi.Gas += 1  
			
		elif curses.KEY_DOWN  == stdscr.nodelay(1):
			if tobi.Gas >= 0:
				tobi.Gas = 0
			elif tobi.Gas > 0:
				tobi.Gas -= 1   
   

	

	except KeyboardInterrupt:
		#wrapper()
		#curses.endwin()
		print "und tschüss"
		key = input ()
		

print "angekommen"
#wrapper()
#curses.endwin()
print "und tschüss"
key = input ()
