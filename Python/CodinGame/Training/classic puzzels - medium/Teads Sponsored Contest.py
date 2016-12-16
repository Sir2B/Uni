import sys
import math
from collections import defaultdict


def find_ends(dictionary):
    for key, value in dictionary.items():
        if len(value) == 1:
            yield key


def find_next_item(dictionary, item):
    liste = dictionary[item]
    if len(liste) == 1:
        return liste[0]

n = int(raw_input())
n_dict = defaultdict(list)
for i in xrange(n):
    xi, yi = [int(j) for j in raw_input().split()]
    n_dict[xi].append(yi)
    n_dict[yi].append(xi)
    
time = 0
points = list(find_ends(n_dict))
print >> sys.stderr, points

while len(points) != 1:
    print >> sys.stderr, n_dict
    new_points = []
    for point in points:
        new_point = find_next_item(n_dict, point)
        if new_point is None:
            continue
        del n_dict[point]
        n_dict[new_point].remove(point)
        new_points.append(new_point)
    points = list(set(new_points))
    print >> sys.stderr, points
    time += 1
    
print time


def find_minimal_time(n_dict):
    start_number = None
    minimal_time = float('inf')
    for start_key in n_dict:
        time = 0
        keys = [start_key]
        used_keys = [start_key]
        while(True):
            next_keys = []
            for key in keys:
                next_keys.extend(n_dict[key])
            keys = [k for k in next_keys if k not in used_keys]
            used_keys.extend(keys)
            if not keys:
                break
            time += 1
        # print >> sys.stderr, "{0}: {1} hours".format(start_key, time)
        if time < minimal_time:
            minimal_time = time
            start_number = start_key
    
# print >> sys.stderr, n_dict
# print minimal_time

