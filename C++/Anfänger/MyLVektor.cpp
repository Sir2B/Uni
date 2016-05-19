#include "MyLVektor.h"
#include <cmath>

MyLVektor::MyLVektor():
	My3Vektor(), t(0)
{}

MyLVektor::MyLVektor(double a1, double a2, double a3, double a4):
	My3Vektor(a2, a3, a4), t(a1)
{}

double MyLVektor::Mass()
{
	return (sqrt(t*t-x*x-y*y-z*z));
}

double MyLVektor::invMass(MyLVektor p)
{
	return(sqrt((p.t+t)*(p.t+t)-(p.x+x)*(p.x+x)-(p.y+y)*(p.y+y)-(p.z+z)*(p.z+z)));
}

double MyLVektor::T()
{
	return t;
}

MyLVektor MyLVektor::Add(MyLVektor a)
{	
	MyLVektor tmp;
	tmp.x = x+a.x;
	tmp.y = y+a.y;
	tmp.z = z+a.z;
	tmp.t = t+a.t;
	return tmp;
}
