#import math

F=[0,1]

for i in range(2,100):
	F.append(F[i-1]+F[i-2])
	
print F, "\n\n"


for n in range(1,99):
	if (F[n+1]*F[n-1]-F[n]**2) != ((-1)**n):
		print "ungleich", n
		break
	else:
		pass
		#print "gleich", n
else:
	print "F[n+1]*F[n-1]-F[n]**2 = (-1)**n"
	
