import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())  # the number of temperatures to analyse
temps = [int(temp) for temp in raw_input().split()]  # the n temperatures expressed as integers ranging from -273 to 5526

print >> sys.stderr, "len(temps): {0}, temps: {1}".format(n, temps)

if n == 0:
    print 0
else:
    result_temp = temps[0]
    for temp in temps[1:]:
        if abs(temp) < abs(result_temp):
            result_temp = temp
        elif temp == (-result_temp):
            result_temp = abs(temp)
    print result_temp
# Write an action using print



