import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in raw_input().split()]
room = []
for i in xrange(h):
    line = raw_input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    room.append([int(s) for s in line.split()])
ex = int(raw_input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).


print >> sys.stderr, room

# game loop
while True:
    xi, yi, pos = raw_input().split()
    xi = int(xi)
    yi = int(yi)

    cell = room[yi][xi]
    print >> sys.stderr, xi, yi, pos, cell
    
    if pos == "TOP":
        if cell in [1,3,7,9]:
            yi += 1
        elif cell in [5,11]:
            xi += 1
        elif cell in [4, 10]:
            xi -= 1
    elif pos == "LEFT":
        if cell in [2, 6]:
            xi += 1
        elif cell in [1, 5, 8, 9, 13]:
            yi += 1
    elif pos == "RIGHT":
        if cell in [2, 6]:
            xi -= 1
        elif cell in [1, 4, 7, 8, 12]:
            yi += 1
            
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print "{0} {1}".format(xi, yi)

