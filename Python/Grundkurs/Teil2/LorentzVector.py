#
import math
#
from ThreeVec import ThreeVec

class LorentzVector(object):
	def __init__ (self, E=0., x=0., y=0., z=0.):
		self.v3 = ThreeVec(x,y,z)
		self.E = E
	def Add (self, tv):
		w = self.v3 + tv.v3 # add ThreeVectors first
		newvec = LorentzVector(self.E+tv.E, w.x, w.y, w.z)
		return newvec
	def Angle( self, tv ):
		return( self.v3.Angle( tv.v3)) # use ThreeVector Method
	def Mass (self):
		return math.sqrt(self.E**2-ThreeVec.ScalarProduct(self.v3, self.v3))
	def InvMass (self, tv):
		return math.sqrt((self.E+tv.E)**2-ThreeVec.ScalarProduct((self.v3+tv.v3),(self.v3+tv.v3)))
	def __str__ (self):
		return '('+str(self.E)+', '+str(self.v3.x)+', '+str(self.v3.y)+', '+str(self.v3.z)+')'


def main():
	print "LorenzVector"
	
if __name__ == "__main__" :
	main()
