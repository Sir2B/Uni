import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in raw_input().split()]
    opponent_x, opponent_y = [int(i) for i in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    if next_checkpoint_angle > 90 or next_checkpoint_angle < -90:
        thrust = 0
    else:
        thrust = 100

        
    boost_angel = 5
    if (-boost_angel) < next_checkpoint_angle < boost_angel:
        if next_checkpoint_dist > 10000:
            thrust = "BOOST"
        
    if next_checkpoint_dist < 600:
        thrust = 0

    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
    print "{0} {1} {2}".format(
        next_checkpoint_x, next_checkpoint_y, thrust)
