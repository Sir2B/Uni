import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
h = int(raw_input())
text = raw_input()
text_ord = [ord(ch)-65 for ch in list(text.upper())]
print >> sys.stderr, text
print >> sys.stderr, text_ord

for i in xrange(h):
    row = raw_input()
    #print >> sys.stderr, row
    list_row = list(row)
    #print >> sys.stderr, list_row

    line = ""
    for char in text_ord:
    	if char > 26 or char < 0:
    		char = -1
    	char_start_position = char*(l)
    	# print >> sys.stderr, char_start_position
    	for i in xrange(l):
    		pass
    		line+=list_row[char_start_position+i]
    print line


# Write an action using print


#print "answer"
