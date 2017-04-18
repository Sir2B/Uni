from ThreeVec import ThreeVec

import random # random numbers

tvc = [] # empty list
for i in range(10000000):
    # create random ThreeVec
    u = ThreeVec( random.gauss(0,1), random.gauss(0,1), random.gauss(0,1))
    tvc.append(u) # store in list

tvc.sort() # sort ThreeVec-list

	

	
for tv in tvc:
    print tv.Length(), tv # output length and Threevec (via __str__())
