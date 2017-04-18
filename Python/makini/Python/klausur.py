 
def sum(n):
	s = 0
	for i in range(n):
		s += i+1
	return s
	
def main ():
	print ("Zahl: ")
	n = input()
	summe=sum(n)
	print " Summe von 1 bis %f ist: %f" %(n, summe)
	
	
if __name__ == '__main__':
	main()
