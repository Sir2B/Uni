#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f = open(sys.argv[1])
zeilen = f.readlines()
print "Anzahl Zeilen:", len(zeilen)

anzahl_woerter= 0
for zeile in zeilen:
    anzahl_woerter += len(zeile.split(' '))

print "Anzahl Wörter:", anzahl_woerter

anzahl_zeichen = 0
for zeile in zeilen:
    anzahl_zeichen += len(zeile)

print "Anzahl Zeichen:", anzahl_zeichen

