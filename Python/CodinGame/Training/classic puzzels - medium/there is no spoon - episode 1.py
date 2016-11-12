import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis

matrix = []
for i in xrange(height):
    line = raw_input()  # width characters, each either 0 or .
    matrix.append([dot=='0' for dot in line])
    print >> sys.stderr, line 

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr, matrix 

for i_row in xrange(len(matrix)):
	for i_collum in xrange(len(matrix[0])):
		if matrix[i_row][i_collum]:
			x1, y1 = i_collum, i_row
			for i2_collum in xrange(i_collum+1, len(matrix[0])):
				if matrix[i_row][i2_collum]:
					x2, y2 = i2_collum, i_row
					break
			else:
				x2, y2 = -1, -1
			for i2_row in xrange(i_row+1, len(matrix)):
				if matrix[i2_row][i_collum]:
					x3, y3 = i_collum, i2_row
					break
			else:
				x3, y3 = -1, -1
			print " ".join([str(i) for i in [x1, y1, x2, y2, x3, y3]])


# Three coordinates: a node, its right neighbor, its bottom neighbor
print "0 0 1 0 0 1"
