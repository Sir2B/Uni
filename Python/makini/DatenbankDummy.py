class _DatenBank:
	def __init__(self):
		self.ID_List = []
		
		
	def ReadUser(self,ID):
		import time
		#Wenn ID stimmt:
		#WriteDate(ID,time.time())
	
	def WriteDate(self,ID, Uhrzeit):
		self.ID_List.append([ID,Uhrzeit])
		print (self.ID_List)