#
import math

from ThreeVec import ThreeVec

u =  ThreeVec( 1., 0.5, 2.)
v =  ThreeVec( 1., 2.5, -1.)
t =	 ThreeVec()
w = u+v
#w = u.Add(v)
r = u.CrossProduct(v)
x = w.ScalarProduct(v)
angle = w.Angle(u)
print "Winkel:",angle
print u
