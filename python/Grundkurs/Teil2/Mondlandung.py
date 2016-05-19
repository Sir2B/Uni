# -*- coding: utf-8 -*-
import math
import pygame
import time
import sys

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

class Lander(object):
	def __init__ (self, m = 1., t = 0., h = 0.):
		self.Leermasse = m
		self.Treibstoff = t
		self.Masse = self.Leermasse + self.Treibstoff
		self.Hoehe = h
		self.Speed = 0
		self.Gas = 0
		self.Gravitation = 0
		self.SpeedFuel = 100

	def Schritt (self,zeit,g,gas):
		self.Gas = gas
		self.beschl = self.Gas * 50
		self.Gravitation = g
		self.Treibstoff -= gas
		self.a = self.Gravitation - self.beschl
		self.Speed += self.a*zeit
		self.Masse += self.Treibstoff
		self.Hoehe = self.Hoehe - self.Speed*zeit


tobi = Lander (100,100,100)
quantisierung = 0.03
g = 5.2
Gas = 0

def main():
	Gas = 0
	pygame.init()
	fpsClock = pygame.time.Clock()
	screen = pygame.display.set_mode((640, 480))
	pygame.key.set_repeat()
	pygame.display.set_caption('Die Mondlandung')

	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))
	
	
	font = pygame.font.Font(None, 22)
	text1 = font.render("", 1, (0, 0, 0))
	textpos1 = text1.get_rect()
	#textpos1.centerx = background.get_rect().centerx
	background.blit(text1, textpos1)
	
	screen.blit(background, (0, 0))
	
	aktiv = True
	while aktiv:
		clock = pygame.time.Clock()
		clock.tick(30)
		TextAnzeige = "Hoehe: %5.2f, Geschwindigkeit: %7.2f, Treibstoff: %7.2f, Gas: %5.2f" %(tobi.Hoehe, tobi.Speed,tobi.Treibstoff, Gas)
		#TextAnzeige = str(Gas)
		text2 = font.render(TextAnzeige, 1, (10, 10, 10))
		screen.blit(background, (0, 0))
		screen.blit(text2, textpos1)
		pygame.display.flip()
		if tobi.Hoehe > 0:
			tobi.Schritt (quantisierung,g,Gas)
		else:
			if tobi.Speed > 5:
				image = pygame.image.load("Crater.jpg")
			else: 
				image = pygame.image.load("Happy.jpg")
			screen.blit(image, (0,20))
			pygame.display.flip()
			aktiv = False
			time.sleep(3)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				aktiv = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					tobi.Hoehe = 100
					tobi.Speed = 0
					tobi.Treibstoff = 100
					Gas = 0
				if event.key == pygame.K_UP:
					Gas += 0.1
					#text = str(Gas)
					#print Gas
				elif event.key == pygame.K_DOWN:
					Gas -= 0.1
				elif event.key == pygame.K_ESCAPE:
					pygame.event.post(pygame.event.Event(pygame.QUIT))
		
		
		#pygame.time.delay(100)
		#time.sleep(0.1)

	
	
	pygame.quit()

if __name__ == '__main__': main()

#while ( tobi.Hoehe > 0):
#	x = raw_input()
#	try:
#		Gas = float(x)
#	except:
#		Gas = 0
#	tobi.Schritt (quantisierung,g,Gas)
#	print "Höhe %4.2f, Geschwindigkeit %4.2f, Treibstoff %4.2f, Gas %4.2f" %(tobi.Hoehe, tobi.Speed,tobi.Treibstoff, tobi.Gas)
#	

print "Höhe %4.2f, Geschwindigkeit %6.2f, Treibstoff %6.2f, Gas %4.2f" %(tobi.Hoehe, tobi.Speed,tobi.Treibstoff, tobi.Gas)
