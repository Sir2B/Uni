import numpy as np

from HOSZ import HOSZ as ho

import time

import matplotlib.pyplot as plt

import scipy.optimize as opt


# --------------------------------------------
# -------------- Aufgabe 1 -------------------
# --------------------------------------------

# Setze N=100, L=10
hosz=ho(100,10)



# -------------- Aufgabe a1) ----------------


# Eigenwerte fuer integer

print '\n', 'Int', '\n'


# initialisiere Matrix
H=hosz.Matrix_HOSZ ('int')

# diagonalisiere Matrix
e, v=np.linalg.eigh(H)

print 'Eigenvalues=', '\n' , e[0:4], ' \n',  '\n'

print 'Float', '\n'



H=hosz.Matrix_HOSZ ('float')


e, v=np.linalg.eigh(H)

print 'Eigenvalues=', '\n' ,e[0:4], ' \n',  '\n'

print 'Complex', '\n'



H=hosz.Matrix_HOSZ ('complex')

e, v=np.linalg.eigh(H)

print 'Eigenvalues=', '\n' , e[0:4], ' \n',  '\n'

# -------------- Aufgabe a2) ----------------

print 'Int', '\n'

# berechne anfangszeit
t0 = time.clock()

H=hosz.Matrix_HOSZ ('int')

e, v=np.linalg.eigh(H)

# berechne endzeit
print 'Elapsed time', time.clock()-t0, '\n', '\n'

print 'Float', '\n'

t0 = time.clock()

H=hosz.Matrix_HOSZ ('float')

e, v=np.linalg.eigh(H)

print 'Elapsed time', time.clock()-t0, '\n', '\n'

print 'Complex', '\n'

t0 = time.clock()

H=hosz.Matrix_HOSZ ('complex')

e, v=np.linalg.eigh(H)

print 'Elapsed time', time.clock()-t0, '\n', '\n'

# --------------------------------------------
# -------------- Aufgabe 2 -------------------
# --------------------------------------------


# -------------- Aufgabe c) ----------------

# L=10
hosz=ho(100,10)
hosz.Vergleich_Lsg_HOSZ()

# L=1
hosz=ho(100,1)
hosz.Vergleich_Lsg_HOSZ()

# -------------- Aufgabe d) ----------------

# Delta_x
Dx=np.zeros(10)

# Delta_E
DE=np.zeros(10)


for nl in range(10):
    # Anzahl Ortspunkte
    N=100*(nl+5)
    # initialisiere Matrixklasse
    hosz=ho(N,100)
    # Berechne numerischen Fehler
    DE[nl]=hosz.Numerischer_Fehler_HOSZ()
    # Berechne Delta_x
    Dx[nl]=100./N


# Plotten
plt.plot(Dx,DE)
plt.suptitle('Numerischer Fehler')
plt.xlabel('D_x')
plt.ylabel('D_E')
plt.show()

# -------------- Aufgabe e) ----------------

# Definiere Polynom
def f(delt, a0,a1,a2, a3, a4):
    return a0 + a1*delt + a2*delt**2 + a3*delt**3 + a4*delt**4


# Fitte Kurve
X,X1=opt.curve_fit(f, Dx, DE)

# Extrahiere Parameter
a0, a1, a2, a3, a4=X

print "Ordnung 0" , a0
print "Ordnung 1" , a1
print "Ordnung 2" , a2
print "Ordnung 3" , a3
print "Ordnung 4" , a4

# Gefittete Funktion fuer Dx
DE_fitted=f(Dx,a0,a1,a2, a3, a4)

# Plotten
plt.plot(Dx,DE, label='Data')
plt.plot(Dx,DE_fitted, label='Fit')
plt.xlabel('D_x')
plt.ylabel('D_E')
plt.legend()
plt.show()

