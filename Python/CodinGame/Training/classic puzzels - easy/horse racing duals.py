import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

strengths = []
n = int(raw_input())
for i in xrange(n):
    pi = int(raw_input())
    strengths.append(pi)

strengths.sort()

nearest_str = float('inf')
for i in xrange(len(strengths)-1):
    dif = abs(strengths[i]-strengths[i+1])
    if dif < nearest_str:
        nearest_str = dif

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print nearest_str
