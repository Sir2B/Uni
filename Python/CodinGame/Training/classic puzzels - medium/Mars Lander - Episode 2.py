import sys
import math

surface_n = int(raw_input()) 
previous_y = None
previous_x = None
for i in xrange(surface_n):
    land_x, land_y = [int(j) for j in raw_input().split()]
    print >> sys.stderr, land_x, land_y
    if land_y == previous_y:
        landing_y = land_y
        landing_x = (previous_x, land_x)
    previous_y = land_y
    previous_x = land_x

print >> sys.stderr, landing_y, landing_x
landing_x_optimum = (landing_x[0]+landing_x[1])//2
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in raw_input().split()]
    print >> sys.stderr, "h_speed: ", h_speed, " v_speed: ", v_speed
    
    angel = 0
    power = 3
    diff = x-landing_x_optimum
    height = y-landing_y
    print >> sys.stderr, "diff: ", diff, " height: ", height
    
    if abs(diff) > 500:
        if v_speed < 0:
            power = 4
        if h_speed < 30 and diff<0:
            angel = -30
        elif h_speed > -30 and diff>0:
            angel = 30
        if abs(h_speed) >= 50:
            angel = 15*h_speed/abs(h_speed)
        if abs(diff) < 1500 and abs(h_speed) >= 20:
            angel = 15*h_speed/abs(h_speed)
            speed = 3
    else:
        if v_speed < -40 or (v_speed < -10 and height<1000) or abs(h_speed) > 30:
            power = 4
        else: 
            power = 2
        
        if h_speed < -20:
            angel = -70
        elif h_speed > 20:
            angel = 70
    if v_speed <= -40:
        angel = 0
    
    if height < 250 and (landing_x[0] < x < landing_x[1]):
        angel = 0

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print "{0} {1}".format(angel, power)