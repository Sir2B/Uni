import sys
import math
from collections import defaultdict, Counter


class Node(object):
	def __init__(self):
		# self.name = name
		self.steps = 1
		self.childs = []

n = int(raw_input())  # the number of relationships of influence
nodelist = defaultdict(Node)
ys = list()
xs = list()
end_points = list()
start_points = list()


def set_steps_for_childs(node):
	for child_name in node.childs:
		child = nodelist[child_name]
		steps = node.steps + 1
		if steps > child.steps:
			child.steps = steps
		set_steps_for_childs(child)



for i in xrange(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in raw_input().split()]
    nodelist[x].childs.append(y)
    xs.append(x)
    ys.append(y)

    print >> sys.stderr, x, y

for x in xs:
	if not x in ys:
		if not x in start_points:
			start_points.append(x)


print >> sys.stderr, start_points

for start_name in start_points:
	node = nodelist[start_name]
	set_steps_for_childs(node)

print >> sys.stderr, [node.steps for node in nodelist.values()]

print max(node.steps for node in nodelist.values())