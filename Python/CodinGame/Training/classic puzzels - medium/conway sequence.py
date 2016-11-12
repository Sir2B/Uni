import sys
import math

r = int(raw_input())
l = int(raw_input())

last_line = [r]
for _ in xrange(l-1):
    line = []
    last_number = None
    last_number_c = 0
    for number in last_line:
        if number == last_number:
            last_number_c += 1
        else:
            if last_number_c != 0:
                line.append(last_number_c)
                line.append(last_number)
            last_number_c = 1
            last_number = number
    else:
        if last_number != 0:
            line.append(last_number_c)
            line.append(last_number)
    last_line = line
        
print >> sys.stderr, last_line
print " ".join(str(n) for n in last_line)
