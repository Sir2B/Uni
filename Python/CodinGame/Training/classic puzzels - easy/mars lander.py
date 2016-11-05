import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(raw_input())  # the number of points used to draw the surface of Mars.
for i in xrange(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in raw_input().split()]

start_thrust = False
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    time = 1
    mars_g = - 3.711
    # next_y = y + 0.5*mars_g*time*time + v_speed*time
    # next_v = v_speed + mars_g*time

    # if not start_thrust:
    #     possible_y = v_speed*math.sqrt(2*y/(mars_g+4)) + y
    #     if possible_y < 0:
    #         start_thrust = True
    #     print >> sys.stderr, "possible_y {0}".format(possible_y)

    rotate = 0
    thrust = 0

    # # if (possible_y < 0):
    # #   thrust = 4
    # #   if v_speed*(mars_g+thrust)*time >= 0:
    # #       thrust = 3

    # if start_thrust:
    #     thrust = 4
    #     while True:
    #         if v_speed*(mars_g+thrust)*time >= 0:
    #             thrust -=1
    #         else:
    #             break

    v_final = v_speed + math.sqrt(2*y*(mars_g+4))
    if v_final < 0:
        thrust = 4

    if y < 1500:
        thrust = 4

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    print "{0} {1}".format(rotate, thrust)
