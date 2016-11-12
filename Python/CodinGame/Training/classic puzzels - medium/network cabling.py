import sys
import numpy as np

n = int(raw_input())
ys = []
xs = []
for i in xrange(n):
    x, y = [int(j) for j in raw_input().split()]
    xs.append(x)
    ys.append(y)
y_main = np.median(ys)
print >> sys.stderr, y_main
cable = max(xs)-min(xs)
for y in ys:
    cable += abs(y-y_main)

print int(cable)
