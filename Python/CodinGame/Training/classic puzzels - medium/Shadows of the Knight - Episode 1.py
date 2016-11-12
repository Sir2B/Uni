import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]


print >> sys.stderr, w
x_min = 0
x_max = w-1
y_min = 0
y_max = h-1

print >> sys.stderr, x_min, x_max, y_min, y_max

# game loop
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if "U" in bomb_dir:
        y_max = y0-1
    elif "D" in bomb_dir:
        y_min = y0+1
    else:
        y_min = y0
        y_max = y0
    
    if "R" in bomb_dir:
        x_min = x0+1
    elif "L" in bomb_dir:
        x_max = x0-1
    else:
        x_min = x0
        x_max = x0
        
    print >> sys.stderr, x_min, x_max, y_min, y_max
        
    x0 = (x_min+x_max)//2
    y0 = (y_min+y_max)//2
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."


    # the location of the next window Batman should jump to.
    print("{0} {1}".format( x0, y0))

