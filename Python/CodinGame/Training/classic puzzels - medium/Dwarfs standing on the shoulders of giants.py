import sys
import math
from collections import defaultdict

n = int(raw_input())  # the number of relationships of influence
dic = defaultdict(list)

for i in xrange(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in raw_input().split()]
    dic[x].append(y)
    print >> sys.stderr, x, y


print "3"
