#!/usr/bin/env python

import math
from ThreeVec import ThreeVec


		
class LorentzVector(ThreeVec):
	def __init__ (self,E = 0. ,x = 0., y = 0., z = 0.):
		ThreeVec.__init__(self,x,y,z)
		self.E = E
	def Add (self , tv ):
		newvec = LorentzVector (self.E+tv.E, tv.x+self.x,tv.y+self.y,tv.z+self.z)
		return newvec
	def __add__ (self, tv):
		newvec = LorentzVector (self.E+tv.E, tv.x+self.x,tv.y+self.y,tv.z+self.z)
		return newvec
	def Sub (self, tv):
		newvec = LorentzVector( self.E-tv.E, self.x-tv.x, self.y - tv.y, self.z-tv.z)
		return newvec;
	def __sub__ (self, tv):
		newvec = LorentzVector( self.E-tv.E, self.x-tv.x, self.y - tv.y, self.z-tv.z)
		return newvec;
	def __str__ (self):
		stringo = ThreeVec.__str__(self)
		s4 = str(self.E)
		stringo += "\n" + s4
		return stringo 
	def Mass (self):
		Masse = math.sqrt(self.E**2 - ThreeVec.ScalarProduct(self,self))
		return Masse
	def InvMass(self, lv):
		E1 = (self.E+lv.E)*(self.E+lv.E)
		Pvec = (ThreeVec.Add(self,lv))
		P1 = ThreeVec.ScalarProduct(Pvec,Pvec)
		return (E1-P1)**0.5

a = LorentzVector(45.0002,0.,0.,45.0)
b = LorentzVector(45.0002,31.8198,0.,31.8198)



print "Angle = " , a.Angle(b)
print "Mass a = " , a.Mass()
print "Mass b = " , b.Mass()
print "Mass a+b = " , b.InvMass(a)
