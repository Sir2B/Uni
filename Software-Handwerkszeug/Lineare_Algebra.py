#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 2 Vektoren
a = [0.3, 1.8, -2.2]
b = [-2.5, 3.8, 0.4]


# Skalarprodukt
Skalarprodukt = 0
for i in range(len(a)):
	Skalarprodukt += a[i]*b[i]
	
print "Skalarprodukt von", a ,"und", b, "ist", Skalarprodukt

# Vektorprodukt
Vektorprodukt = [0,0,0]
for i in range(3):
	Vektorprodukt[i]=a[((i+1)%3)]*b[((i+2)%3)]-a[((i+2)%3)]*b[((i+1)%3)]

print "Vektorprodukt von", a ,"und", b, "ist", Vektorprodukt

# 2 Matrizen
C = [ [ 0.61, 0.24, 1.16 ], [ 0.14, -0.82, 0.92 ], [ -1.25, 0.96, -0.23 ] ] 
D = [ [ 0.40, -0.68, -0.68 ], [ 0.65, -0.75, 0.23 ], [ 0.52, 0.51, 0.31 ] ]

# Matrixmultiplikation
M = [[0]*len(C) for i in range(len(D))]

for i in range(len(C)):
	for j in range(len(D)):
		for n in range(len(C)):
			M[i][j] += C[i][n] * D[n][j]
			
print M
		
