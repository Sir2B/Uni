import sys
import math
from collections import defaultdict

n = int(raw_input())
dict = defaultdict(list)
for i in xrange(n):
    xi, yi = [int(j) for j in raw_input().split()]
    dict[xi].append(yi)
    dict[yi].append(xi)

start_number = None
minimal_time = float('inf')
for start_key in dict:
    time = 0
    keys = [start_key]
    used_keys = [start_key]
    while(True):
        next_keys = []
        for key in keys:
            next_keys.extend(dict[key])
        keys = [k for k in next_keys if k not in used_keys]
        used_keys.extend(keys)
        if not keys:
            break
        time += 1
    print >> sys.stderr, "{0}: {1} hours".format(start_key, time)
    if time < minimal_time:
        minimal_time = time
        start_number = start_key
    
print >> sys.stderr, dict
print minimal_time
