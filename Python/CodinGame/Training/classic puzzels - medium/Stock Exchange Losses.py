import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
array = []
for i in raw_input().split():
    v = int(i)
    array.append(v)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
# print >> sys.stderr, array

def max_diff(array):
    max_loss = 0
    for index in xrange(n):
        for index2 in xrange(index+1, n):
            loss = array[index2]-array[index]
            if loss < max_loss:
                max_loss = loss
    return max_loss


def max_diff_2(array):
    maxi = array[0]
    diff = 0
    for value in array:
        if value > maxi:
            maxi = value
        if value - maxi < diff:
            diff = value - maxi
    return diff
    
    
print max_diff_2(array)
