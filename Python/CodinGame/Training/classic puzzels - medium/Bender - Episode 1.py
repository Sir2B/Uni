import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def can_go(obstacle):
    if obstacle == "#":
        return False
    elif obstacle == "X":
        if breaker_mode:
            breaker_mode = False
            return True
        return False
    return True
    
def redeem_obstacle(obstacle):
    if obstacle == "B":
        breaker_mode = True
    elif obstacle == "T":
        pass
    elif obstacle == "I":
        next_direction = next_direction[::-1]
    elif obstacle == "$":
        running = False
    elif obstacle == "S":
        bender_dir = "SOUTH"
    elif obstacle == "E":
        bender_dir = "EAST"
    elif obstacle == "W":
        bender_dir = "WEST"
    elif obstacle == "N":
        bender_dir = "NORTH"
        
next_direction = ["SOUTH", "EAST", "NORTH", "WEST"]

direction_map = {"SOUTH": (0,1), "EAST": (1,0), 
                "NORTH": (0,-1), "WEST":(-1,0)}

bender_map = []
bender_pos = ()
bender_dir = "SOUTH"
breaker_mode = False
l, c = [int(i) for i in raw_input().split()]
for y in xrange(l):
    row = raw_input()
    bender_map.append(row)
    if "@" in row:
        x = row.index("@")
        bender_pos = (x, y)
    
print >> sys.stderr, bender_map, bender_pos
running = True
next_direction_i = 0
while (running):
    direction = direction_map[bender_dir]
    next_pos = bender_pos[0]+direction[0],bender_pos[1]+direction[1]
    next_obs = bender_map[next_pos[0]][next_pos[1]]
    
    if can_go(next_obs):
        print >> sys.stderr, "Obs: {0}".format(next_obs)
        redeem_obstacle(next_obs)
        bender_pos = next_pos
        print bender_dir
    else:
        bender_dir = next_direction[next_direction_i]
        next_direction_i += 1

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print "answer"
