#
import math
#

class ThreeVec(object):
	"Class for 3 Vector and operations"
	def __init__( self, x=0., y=0., z=0.):
		self.x = x
		self.y = y
		self.z = z
	def Add( self, tv ): # add two 3 vecs
		newvec = ThreeVec( self.x+tv.x, self.y+tv.y, self.z+tv.z)
		return newvec
	def Length( self ): # 
		return math.sqrt( self.x**2 + self.y**2 + self.z**2 )
	def Scale( self, a ): # Skalierung mit float
		newvec = ThreeVec(self.x*a, self.y*a, self.z*a)
	def Angle( self, a ): # Winkel zwischen 2 Threevectors
		return math.acos(self.ScalarProduct(a)/(self.Length()*a.Length()))
	def ScalarProduct( self, a ): # Skalarprodukt von 2 Threevectors
		return (self.x*a.x + self.y*a.y + self.z*a.z)

	def CrossProduct( self, a ): # Kreuzprodukt von 2 Threevectors
		newvec = ThreeVec(self.y*a.z-self.z*a.y, self.z*a.x-self.x*a.z, self.x*a.y-self.y*a.x)
		return newvec

	def __add__( self, tv ):
		return self.Add(tv)
	def __sub__( self, tv ):
		return self.Add(tv.Scale(-1.))	
	def __mul__( self, tv ):
		return self.Scale(tv)
	def __rmul__( self, tv ):
		return self.Scale(tv)
	def __str__(self):
		#return '('+str(self.x)+', '+str(self.y)+', '+str(self.z)+')'
		return '(%6.3f, %6.3f, %6.3f)' %(self.x, self.y, self.z)
	def __cmp__ (self, tv):
		if self.Length() == tv.Length(): return 0
		elif self.Length() < tv.Length(): return -1
		else: return 1
	
def main():
	print "ThreeVec"
	
if __name__ == "__main__" :
	main()
