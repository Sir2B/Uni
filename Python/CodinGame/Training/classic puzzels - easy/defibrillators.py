import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = raw_input()
lat = raw_input()
n = int(raw_input())

lon = float(lon.replace(',', '.'))
lat = float(lat.replace(',', '.'))


nearest_name = ""
nearest_dist = float('inf')
for i in xrange(n):
    defib = raw_input()
    
    i, name, adr, num, lon_def, lat_def = defib.split(";")
    lon_def = float(lon_def.replace(',', '.'))
    lat_def = float(lat_def.replace(',', '.'))

    x = (lon_def - lon) *math.cos((lat+lat_def)/2.)
    y = lat_def - lat
    dist = math.sqrt(x*x+y*y)
    print >> sys.stderr, name, dist
    print >> sys.stderr, nearest_dist
    if dist < nearest_dist:
        nearest_dist = dist
        nearest_name = name

print nearest_name



# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
