import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

center = [8000, 4500]

boostUsed = False;

def distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    
    
checkpoint_list = []
first_lap = True
starting_time = True
def detect_next_checkpoint(current_checkpoint):
    global first_lap
    print >> sys.stderr, checkpoint_list, first_lap

    
    if first_lap:
        if len(checkpoint_list) == 0:
            checkpoint_list.append(current_checkpoint)
        elif len(checkpoint_list) == 1:
            if current_checkpoint != checkpoint_list[-1]:
                checkpoint_list.append(current_checkpoint)
        else:
            if current_checkpoint == checkpoint_list[0]:
                first_lap = False
            elif current_checkpoint != checkpoint_list[-1]:
                checkpoint_list.append(current_checkpoint)
        return center[:]
    
    index_current = checkpoint_list.index(current_checkpoint)
    return checkpoint_list[(index_current+1) % len(checkpoint_list)][:] # copy to avoid changes
            
def calc_pos(rounds, position, last_pos):
    x = position[0] + rounds * (position[0] - last_pos[0])
    y = position[1] + rounds * (position[1] - last_pos[1])
    return [x, y]

last_x = None
last_y = None

last_x_opponent = None
last_y_opponent = None
# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in raw_input().split()]
    opponent_x, opponent_y = [int(i) for i in raw_input().split()]
    
    print >> sys.stderr, "x, y: ", x, y
    print >> sys.stderr, "opponent x, y: ", opponent_x, opponent_y
    
    print >> sys.stderr, "checkpoint x, y: ", next_checkpoint_x, next_checkpoint_y
    print >> sys.stderr, "checkpoint dist, angel: ", next_checkpoint_dist, next_checkpoint_angle
    

    print >> sys.stderr, " boostUsed", boostUsed
    
    target = [next_checkpoint_x, next_checkpoint_y]
    
    if next_checkpoint_angle > 60 or next_checkpoint_angle < -60:
        print >> sys.stderr, "over 60 degrees"
        thrust = 0
    elif next_checkpoint_dist < 1000 and (next_checkpoint_angle > 40 or next_checkpoint_angle < -40):
        print >> sys.stderr, "over 40 degrees"
        thrust = 0
    else:
        thrust = 100

        
    # boost_angel = 3
    # if (-boost_angel) < next_checkpoint_angle < boost_angel:
    #     if next_checkpoint_dist > 8000 and not boostUsed:
    #         thrust = "BOOST"
    #     elif not first_lap and not boostUsed and next_checkpoint_dist > 4000:
    #         thrust = "BOOST"
    if starting_time:
        starting_time = False
        if next_checkpoint_dist > 4000:
            thrust = "BOOST"
    elif next_checkpoint_dist > 8000 and not boostUsed:
        thrust = "BOOST"
    elif not first_lap and not boostUsed and next_checkpoint_dist > 4000:
        thrust = "BOOST"
        
    # if next_checkpoint_dist < 800:
    #     thrust = 1
        
    next_target = detect_next_checkpoint([next_checkpoint_x, next_checkpoint_y])
    if last_x and last_y:
        next_pos = calc_pos(2, [x,y], [last_x, last_y])
        if distance(next_pos[0], next_pos[1], next_checkpoint_x, next_checkpoint_y) < 600:
            target = next_target
            thrust = 30
        
        next_pos = calc_pos(1, [x,y], [last_x, last_y]) 
        next_pos_opponent = calc_pos(1, [opponent_x,opponent_y], [last_x_opponent, last_y_opponent])   
        
        dist_to_opponent = distance(next_pos[0], next_pos[0], next_pos_opponent[0], next_pos_opponent[1])
        
        print >> sys.stderr, "distance:", dist_to_opponent
        print >> sys.stderr, "next pos:", next_pos
        print >> sys.stderr, "next pos opponent:", next_pos_opponent
        if dist_to_opponent < 400:
            print >> sys.stderr, "SHIELD!!!"
            #thrust = "SHIELD"
        
        dx = x - last_x
        dy = y - last_y
        
        if dx != 0:
        
            time = (target[0] - x) / dx
            if time > 0:
                print >> sys.stderr, "time:", time
                landing_y = y + time * dy
                
                new_target_y = 2*target[1] - landing_y
                print >> sys.stderr, "old y, new_y:", target[1], new_target_y
                
                target[1] = new_target_y
        

    if thrust == "BOOST":
        boostUsed = True
    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print "{0} {1} {2}".format(
        target[0], target[1], thrust)
        
    last_x = x
    last_y = y
    last_x_opponent = opponent_x
    last_y_opponent = opponent_y
    