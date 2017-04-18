#!/usr/bin/python
# -*- coding: utf-8 -*.

from email.parser import Parser
import smtplib
import sys
from Kommunikation import *
import time

def main(argv):
	to = []
	to.append('tobias.obermayer@gmail.com')
	to.append('marweb@alice.de')
	to.append('weberol@alice-dsl.net')

	user = 'myraspberry@web.de'
	passwort= '76b5hgB3cpZvp!^u!BTy'
	i = 0
	while i < 1:
		try:
			SensornameZuTemperatur = GetSensornameZuTemperatur()
			subject = 'Temperatur beim Markus in da Stumm'
			text = ""
			for schnipsel in argv:
				text+=schnipsel
			
			headers=[]
			for Adressat in to:
				headers.append(Parser().parsestr(
					'From: ' + user + '\n'
					'To: ' + Adressat + '\n'
					'Subject: ' + subject +'\n'
					'\n'
					+ text + '\n'))



			smtp = smtplib.SMTP(host='smtp.web.de', port=587)
			# smtp.ehlo()
			smtp.starttls()
			# smtp.ehlo()
			smtp.login("myraspberry@web.de", passwort)
			for header in headers:
				smtp.sendmail(header['from'], header['to'], header.as_string())
			#smtp.quit()
			i+=1
			print "Mail versendet an:"
			for Empfaenger in to:
				print Empfaenger
			#time.sleep(2)
		except KeyboardInterrupt:
			exit()

if __name__ == "__main__":
   main(sys.argv[1:])