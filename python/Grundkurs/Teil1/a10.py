import sys
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

def GGT(a, b):
	if ( a%b != 0):	return GGT(b,a%b)
	else: return b

print "GGT von", num1, "und", num2, "ist", GGT(num1, num2)
