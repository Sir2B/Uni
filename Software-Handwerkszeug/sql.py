import sqlite3

o=open('Students.txt')
zeilen=o.readlines()
o.close()

conn = sqlite3.connect('Students.sqlite3', isolation_level='DEFERRED')
curs=conn.cursor()
curs.execute('''SELECT count(*) FROM studenten''')
KEY=curs.fetchone()[0]

for zeile in zeilen:
	wort=zeile.split()
	curs.execute('''INSERT INTO studenten VALUES (?, ?, ?, ?, ?)''', (None, str(wort[0]),str(wort[1]),str(wort[2]),str(wort[3])))
	conn.commit()
	
conn.close()
