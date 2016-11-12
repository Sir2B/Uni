
#!/usr/bin/env python

from cPickle import load, dump

f=open('Students.txt')
zeilen=f.readlines()
f.close()

data={}
for zeile in zeilen:
	temp = zeile.split()
	data[int(temp[2])] = [temp[0],temp[1], float(temp[3])]
	
out = open('data.pickle','wb')
dump(data,out)
out.close()
