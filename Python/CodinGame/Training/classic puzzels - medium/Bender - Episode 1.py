import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def can_go(obstacle, position):
    global breaker_mode
    if obstacle == "#":
        return False
    elif obstacle == "X":
        if breaker_mode:
            remove_obstacle(position)
            return True
        return False
    return True


def remove_obstacle(position):
    global bender_map, map_changed
    map_changed = True
    line = list(bender_map[position[1]])
    line[position[0]] = " "
    bender_map[position[1]] = "".join(line)


def teleport_from(position):
    global teleports, bender_pos
    for t in teleports:
        if t != position:
            bender_pos = t


def is_loop(pose):
    global positions, map_changed
    posi, diri, breakeri, changed = pose
    if posi in positions:
        posi2, diri2, breakeri2, changed2 = positions[posi]
        if changed or changed2 or diri2 != diri or breakeri != breakeri2:
            return False
        return True
    else:
        positions[posi] = (diri, breakeri, changed)
        return False


def redeem_obstacle(obstacle, position):
    global breaker_mode, next_direction, running, bender_dir
    if obstacle == "B":
        breaker_mode = not breaker_mode
    elif obstacle == "T":
        teleport_from(position)
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

direction_map = {"SOUTH": (0, 1), "EAST": (1, 0),
                 "NORTH": (0, -1), "WEST": (-1, 0)}

bender_map = []
bender_pos = ()
teleports = []
bender_dir = "SOUTH"
breaker_mode = False
loop = False
map_changed = False
l, c = [int(i) for i in raw_input().split()]
for y in xrange(l):
    row = raw_input()
    bender_map.append(row)
    if "@" in row:
        x = row.index("@")
        bender_pos = (x, y)
    elif "T" in row:
        x = row.index("T")
        teleports.append((x, y))

print >> sys.stderr, bender_map, bender_pos
running = True
next_direction_i = 0
directions = []
positions = {}
while running:
    direction = direction_map[bender_dir]
    next_pos = bender_pos[0] + direction[0], bender_pos[1] + direction[1]
    next_obs = bender_map[next_pos[1]][next_pos[0]]

    if can_go(next_obs, next_pos):
        next_direction_i = 0
        # print >> sys.stderr, "Obs: {0}".format(next_obs)
        directions.append(bender_dir)

        pos = (bender_pos, bender_dir, breaker_mode, map_changed)

        if is_loop(pos):
            running = False
            loop = True
        positions[bender_pos] = pos
        bender_pos = next_pos
        redeem_obstacle(next_obs, next_pos)
    else:
        bender_dir = next_direction[next_direction_i]
        next_direction_i += 1

if loop:
    print "LOOP"
else:
    for d in directions:
        print d
