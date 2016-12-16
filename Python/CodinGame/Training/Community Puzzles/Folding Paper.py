import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

order = raw_input()
side = raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

direction_order = "URLD"
reverse_order = "DLRU"
left_order = "RDUL"
right_order = "LUDR"
layers = [1, 1, 1, 1]

for fold in order:
    layers[reverse_order.index(fold)] += layers[direction_order.index(fold)]
    layers[direction_order.index(fold)] = 1
    layers[left_order.index(fold)] *= 2
    layers[right_order.index(fold)] *= 2
    
print layers[direction_order.index(side)]
