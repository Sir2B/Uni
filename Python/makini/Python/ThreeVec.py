import math


class ThreeVec:
	def __init__(self, x=0, y = 0, z = 0):
		self.x=x
		self.y=y
		self.z=z
	def Length(self):
		return (math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z))
	def Add (self, tv):
		newvec = ThreeVec( self.x+tv.x, self.y + tv.y, self.z+tv.z)
		return newvec;
	def Sub (self, tv):
		newvec = ThreeVec( self.x-tv.x, self.y - tv.y, self.z-tv.z)
		return newvec;
	def ScalarProduct (self, tv):
		return ( self.x*tv.x+ self.y * tv.y+ self.z*tv.z )
	def CrossProduct (self, tv):
		newvec = ThreeVec (self.y*tv.z- self.z * tv.y, self.z*tv.x- self.x * tv.z,self.x*tv.y- self.y * tv.x)
		return newvec
	def Scale (self, f , tv = 0):
		if tv.Length == 0:
		  self.x *= f
		  self.y *= f
		  self.z *= f
		else:
		  tv.x *=f
		  tv.y *=f
		  tv.z *=f
	def Angle (self, tv):
		a = math.acos ( self.ScalarProduct(tv)/(self.Length() * tv.Length() ))
		return a
	def __add__(self, tv):
		newvec = ThreeVec( self.x+tv.x, self.y + tv.y, self.z+tv.z)
		return newvec;
	def __sub__ (self, tv):
		newvec = ThreeVec( self.x-tv.x, self.y - tv.y, self.z-tv.z)
		return newvec;
	def __str__ (self):

		s1 = str(self.x)
		s2 = str(self.y)
		s3 = str(self.z)
		stringo = "( " + s1 + ", " + s2 + ", " + s3 + " )"
		return stringo
	def __cmp__(self, other):
		v1 = self.ScalarProduct(self)
		v2 = other.ScalarProduct(other)
		if v1 == v2: return 0
		if v1 > v2: return 1
		else: return -1		
