from LorentzVector import LorentzVector

a = LorentzVector(45.0002,0.,0.,45.0)
b = LorentzVector(45.0002,31.8198,0.,31.8198)
print "Angle = " , a.Angle(b)
print "Mass a = " , a.Mass()
print "Mass b = " , b.Mass()
print "Mass a+b = " , b.InvMass(a)
print a
print b
print a.Add(b)
