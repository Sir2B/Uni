#!/usr/bin/env python
import cgi
dictionary = cgi.FieldStorage()

stdout.write("Content-type: text/plain\r\n\r\n")

for key in dictionary.keys():
    print "%s=%s" % (key, dictionary[key])

print "test123"
