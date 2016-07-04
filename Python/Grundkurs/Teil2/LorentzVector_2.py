#
import math
#
from ThreeVec import ThreeVec

class LorentzVec(ThreeVec): # inherits from ThreeVec
	"Class for 4 Vector and operations"
	def __init__( self, t=0., x=0., y=0., z=0.):
		ThreeVec.__init__( self, x, y, z )  # initialize  ThreeVec
		self.t = t
	def Add( self, tv ):
		w = ThreeVec.Add( self, tv ) # call ThreeVec method first
		newvec = LorentzVec(self.t+tv.t,  w.x, w.y, w.z)
		return newvec
	#    def Angle( self, tv ): no need to define here, available from ThreeVec
	def Mass (self):
		return math.sqrt(self.t**2-self.Length()**2)
	def InvMass (self, tv):
		return math.sqrt((self.t+tv.t)**2-ThreeVec.Add(self, tv).Length()**2)
	def __str__ (self):
		return '('+str(self.t)+', '+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'
