__author__ = 'philipp'

import numpy as np
import numpy.linalg as lin
import matplotlib.pyplot as plt
import matplotlib
matplotlib.interactive(True)


def update_positions():
    global phi, phi_dot, phi_ddot, t, l, N
    hx = 0
    hy = 0
    A = np.multiply( np.outer(np.cos(phi),np.cos(phi))+np.outer(np.sin(phi),np.sin(phi)) , M )
    D = -c*np.sin(phi)
    for i in xrange(N):
        D[i]*=(N-i)
    B = np.multiply( np.outer(np.sin(phi),np.cos(phi))-np.outer(np.cos(phi),np.sin(phi)) , M )
    D -= np.dot(B,phi_dot**2)
    phi_ddot=np.dot(lin.inv(A), D)-gamma*phi_dot
    phi_dot=phi_ddot*t + phi_dot
    phi = phi_dot*t+phi
    for j in xrange(N):
        hx += np.sin(phi[j])
        x[j] = x0+l*hx
        hy+=np.cos(phi[j])
        y[j]=y0-l*hy

def Stufenmatrix(N):

    B=np.zeros([N,N])

    for i in xrange(N):
        for j in xrange(N-1,i-1,-1):
            B[j][i]=N-j
            if j == i:
                for k in xrange(j):
                    B[k][j] = N-j
    return B


l=0.9 #Laenge der Pendel
t = 0.0009 #Zeitschritt
N=3 #Anzahl der Pendel
gamma = 0 #Daempfung
g=1 #Erdbeschleunigung

c=g/l
x0=10
y0=10
phi = 6.28*np.random.random_sample((N,)) #Anfangswinkel
phi_dot = 0*np.random.random_sample((N,)) #Anfangs(winkel)geschwindigkeiten
phi_ddot = np.zeros(N) #Anfangs(winkel)beschleunigungen
A=np.zeros([N, N])
D=np.zeros(N)           #A,D,M Hilfsmatrizen
M = Stufenmatrix(N)
x = np.zeros(N)         #x,y: kartesische Koordinaten
y =  np.zeros(N)



plot1 = plt.subplot()
plot1.set_xlim([0, 20])
plot1.set_ylim([0, 20])

data, = plot1.plot(x,y, '-')

for i in range(50000):
    if (i%100==0):
        data.set_xdata(np.insert(x,0,x0))
        data.set_ydata(np.insert(y,0,y0))
        plt.draw()
    update_positions()

