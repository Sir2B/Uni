import numpy as np

from scipy.special import hermite as herm

import matplotlib.pyplot as plt

import math


class HOSZ(object):

    # -----------------------------------------------------------
    # initialisiere die matrix-parameter N, L, Dx und x
    def __init__(object, N, L):
    
        object.N, object.L = N, L
        
        object.Dx=object.L*1.0/object.N
        
        # initialisiere x als ortskoordinate
        object.x=np.zeros(object.N)
        
        for n in range(object.N):
            # Ortskoordinate x_n
            object.x[n]=-object.L/2.0+n*object.Dx

    # ----------------------------------------------------------
    # initialisiere matrix
    def Matrix_HOSZ (object, type):
        
        # berechne 1/(Dx^2)
        Diag=1.0/(object.Dx**2)
        
        # berechne -1/(2*Dx^2)
        Off_Diag=-Diag/2.0
        
        # initialisiere H als NxN Matrix mit Eintraegen=0
        H=np.zeros((object.N, object.N), dtype=type)
        
        for n in range(object.N):
            
            # n-tes Diagonalelement
            H[n,n] =0.5*(object.x[n]**2)+Diag
            
            # H[n+1,n] und H[n-1,n]
            if n<object.N-1:
                H[n+1,n]=Off_Diag
                H[n,n+1]=Off_Diag
    
        # Ausgabe der Matrix H
        return H
    
    # --------------------------------------------------------------
    # Finde Eigenwerte und -vektoren
    
    def Eigensystem_HOSZ(object):
        # initialisiere Matrix
        H=object.Matrix_HOSZ ('float')
        
        # diagonalisiere Matrix (e=Eigenwerte, v=Eigenvektoren)
        e, v=np.linalg.eigh(H)
        
        return(e,v)
    # --------------------------------------------------------------
    # Berechne l-te analytische Loesung
    
    def Analytische_Lsg_HOSZ(object, l):
        # Eigenwert
        El=l+0.5
        
        # Vorfaktor
        Prefact=np.pi**(-1/4)/np.sqrt(math.factorial(l)*(2.0**l))
        
        # Hermitesches Polynom l-ter Ordnung
        Hl=herm(l)
        
        # initialisiere Wellenfunktion
        Psil=np.zeros(object.N)
        
        for i in range(object.N):
            # i-ter Eintrag der Wellenfunktion
            Psil[i]=Prefact*np.exp(-object.x[i]**2/2)*Hl(object.x[i])
        
        # normiere Wellenfunktion auf 1
        Psil /= np.linalg.norm(Psil)
        
        return (El,Psil)

    # --------------------------------------------------------------------
    # Vergleiche analytische und numerische Werte

    def Vergleich_Lsg_HOSZ(object):
        # analytische Eigenwerte
        E=np.zeros(10)
        
        # Matrix mit den ersten 10 analytischen Eigenvektoren
        Psi=np.zeros((object.N,10))
        
        for i in range(10):
            E[i], Psi[:,i]=object.Analytische_Lsg_HOSZ(i) # berechne analytische Ergebnisse

        # Berechne numerische Eigenwerte und -vektoren
        e, v=object.Eigensystem_HOSZ()
        
        # Plotte die ersten 10 Eigenwerte
        
        plt.plot(e[0:10], label='numeric') # plotte numerische Eigenwerte
        
        plt.plot(E, label='analytic') # plotte analytische Eigenwerte
        
        plt.suptitle('L='+str(object.L)) # Plottitel
        
        plt.xlabel('l') # x-Achsenbeschriftung
        
        plt.ylabel('E') # y-Achsenbeschriftung
        
        plt.legend()  # Legende (Plotfarben)
        
        plt.show() # Zeige Plot
        
        # Plotte die ersten 10 Eigenvektoren als Dichte
        for l in range(10):
        
            plt.plot(object.x, np.absolute(v[:,l])**2, label='numeric')
            
            plt.plot(object.x, np.absolute(Psi[:,l])**2, label='analytic')
            
            plt.suptitle('L='+str(object.L))
            
            plt.xlabel('x')
            
            plt.ylabel('n'+str(l)+'(x)')
            
            plt.legend()
            
            plt.show()
        


    # ---------------------------------------------------------------
    # Berechne den numerischen Fehler

    def Numerischer_Fehler_HOSZ(object):
        
        E=np.zeros(10) # Analytische Eigenwerte
        
        for i in range(10):
            E[i], X=object.Analytische_Lsg_HOSZ(i)  # Berechnung analytische Eigenwerte
        
        e, v=object.Eigensystem_HOSZ() # Berechnung numerische Eigenwerte
        
        Delta_E=np.sum(np.absolute(e[0:10]-E)) # Numerischer Fehler
        
        return Delta_E










