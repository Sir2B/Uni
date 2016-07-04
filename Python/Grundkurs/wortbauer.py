#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import random

def ChoiceMaker(Liste):
	maximum = sum([probability for (char, probability) in Wahrscheinlichkeiten.items() if char in Liste])
	random_number = random.random() * maximum
	upto = 0
	for char, probability in Wahrscheinlichkeiten.items():
		if char in Liste:
			if upto + probability > random_number:
				return char
		upto += probability
	else:
		raise Exception

Wahrscheinlichkeiten = dict(e=17.4, n=9.78, i=7.55, s=7.27, r=7.00, a=6.51, t=6.15, d=5.08, h=4.76, u=4.35, l=3.44, c=3.05, g=3.01, m=2.53, 
							o=2.51, b=1.89, w=1.89, f=1.66, k=1.21, z=1.13, p=0.79, v=0.67, ss=0.31, j=0.27, y=0.04, x=0.03, q=0.02)

							
Vokale = ["a", "e", "i", "o", "u"]

Konsonaten = [char for char in string.lowercase if char not in Vokale]

Wortlaenge = random.randint(5,9)

Wort = ""
for i in range(Wortlaenge):
	if i % 2 == 0:
		#Wort += random.choice(Vokale)
		Wort += ChoiceMaker(Vokale)
	else:
		#Wort += random.choice(Konsonaten)
		Wort += ChoiceMaker(Konsonaten)
print Wort
