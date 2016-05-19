#!/usr/bin/python
# -*- coding: utf-8 -*-
#musiknotendatenbank
import sqlite3
import os


Unterordner='Noten'
def aktualisieren():
	conn = sqlite3.connect('Noten.sqlite3', isolation_level='DEFERRED')
	curs=conn.cursor()
	#try:
	#	curs.execute('''DROP TABLE noten_tmp''')
	curs.execute('''ALTER TABLE noten RENAME TO noten_tmp''')

	
	curs.execute('''CREATE TABLE noten (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	Ordner TEXT,
	Nummer INTEGER,
	Stueckname TEXT,
	Instrument TEXT
	);''')

	os.chdir(Unterordner)
	for root, dirs, files in os.walk('.'):
		if len(files) is not 0:
			#print root, dirs, files
			ordner=root.split('/')[1]
			nummer=root.split('/')[2].split('. ')[0]
			stueck=root.split('/')[2].split('. ')[1]
			#name=files[0].split('.jpg')[0]
			for instr in files:
				instrument=instr.split('.jpg')[0]
				#print ordner, nummer, stueck, instrument
				curs.execute('''INSERT INTO noten VALUES (?, ?, ?, ?, ?)''', (None, ordner,int(nummer),stueck,instrument))
				#conn.commit()
	
	#try:
	curs.execute('''DROP TABLE noten_tmp''')
	
	conn.commit()
	conn.close()



def auslesen():
	conn = sqlite3.connect('Noten.sqlite3', isolation_level='DEFERRED')
	curs=conn.cursor()
	
	curs.execute('''SELECT * from noten''')
	result = curs.fetchone()
	while result is not None:
		print result
		result = curs.fetchone()
	conn.close()

#aktualisieren()
auslesen()
