import math

def suche( x1, x2, f ) :
    " suche Nullstelle von Funktion f zwischen x1 und x2"
    f1 = f(x1);
    f2 = f(x2);
    i = 0
    while  i < 1000  : #  Abbruch nach 1000 Iterationen
        xn = (x1+x2)/2.   # Neues x in Mitte
        fn = f(xn);       # Funktionswert dazu
        if  abs(fn) < 1e-6 : break # Konvergenz: 1e-6 an Nullstelle, dann Abbruch

        if  fn*f2 > 0.  :  # gleiches Vorzeichen wir f2 ?
            x2,f2 = xn,fn    #  dann ersetze x2,f2
        else:
            x1,f1 = xn,fn    # andernfalls x1,f1
            
        i = i+1
    else:                    # keine Konvergenz
        print 'Error: Keine Konvergenz fuer Nullstellensuche', fn
        
    return xn 
#
# Test
def myf1(x) :
    return( math.exp(-x) -x);
def myf2(x):
	return (math.exp(x)-pow(x,10))

print suche( 1., 3., math.sin)  # Funktion aus math
#suche( 0., 3., myf1)  # selbst-definierte  Funktion 
#suche( 0., 3., lambda x : math.exp(x) -2. ) # Kurzform mit lambda func
#print suche(-1,1, myf2)
