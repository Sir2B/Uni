import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in raw_input().split()]

links = []
for i in xrange(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in raw_input().split()]
    links.append((n1, n2))
    
print >> sys.stderr, links
links_to_gateways = []
for i in xrange(e):
    ei = int(raw_input())  # the index of a gateway node
    for link in links:
    	if link[0] == ei or link[1] == ei:
    		links_to_gateways.append(link)



# game loop
while True:
    si = int(raw_input())  # The index of the node on which the Skynet agent is positioned this turn
    next_link = links_to_gateways.pop()
    print "{0} {1}".format(links_to_gateways[0], links_to_gateways[1])
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."


    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    #print "0 1"
