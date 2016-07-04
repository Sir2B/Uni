def Sum(n):
	s = 0
	for i in range(0,n+1):
		s += i
	return s
		
def main():
	print "Bitte Zahl eingeben: "
	n = raw_input()
	try:
		n= int(n)
	except:
		print "Keine Zahl"
		main()
	summe= Sum(n)
	print "Summe von 1 bis %s ist : %s" %(n, summe)
	
if __name__ == '__main__':
	main()
