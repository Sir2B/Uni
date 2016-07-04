M=[[0.]*2]*1
try:
    determinant = M[0][0]*M[1][1] - M[0][1]*M[1][0]
except IndexError, x:
    print  "M is the wrong size to have a determinant.",  x
except NameError, x:
    print  "Programming error!  M doesn't exist:  ",  x

#
