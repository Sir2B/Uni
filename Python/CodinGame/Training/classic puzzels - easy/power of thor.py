import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]
thor_x = initial_tx
thor_y = initial_ty
# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    move_x = light_x - thor_x
    move_y = light_y - thor_y

    direction = ""
    if move_y > 0:
    	direction += "S"
    	thor_y += 1
    elif move_y < 0:
    	direction += "N"
    	thor_y -= 1

    if move_x > 0:
    	direction += "E"
    	thor_x += 1
    elif move_x < 0:
    	direction += "W"
    	thor_x -= 1

    # Write an action using print
    print >> sys.stderr, "thors position x: {0}, y: {1}".format(thor_x, thor_y)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print direction
