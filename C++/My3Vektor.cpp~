#include "My3Vektor.h"
#include <cmath>
#include <iostream>
using namespace std;

My3Vektor::My3Vektor()
	{
	x=y=z=0;
	}

My3Vektor::My3Vektor(double a1, double a2, double a3)
	{
	x=a1;
	y=a2;
	z=a3;
	}
	
double My3Vektor::Length()
	{
		return(sqrt(x*x+y*y+z*z));
	}
	
My3Vektor My3Vektor::Add(My3Vektor a)
	{
		My3Vektor t;
		t.x = x +a.x;
		t.y = y +a.y;
		t.z = z +a.z;
		return(t);
	}

double My3Vektor::Skalarprodukt(My3Vektor a)
	{
		return(x*a.x+y*a.y+z*a.z);
	}

My3Vektor My3Vektor::Vektorprodukt(My3Vektor a)
	{
		My3Vektor t;
		t.x = a.y*z-a.z*y;
		t.y = a.z*x-a.x*z;
		t.z = a.x*y-a.y*x;
		return(t);
	}

double My3Vektor::Winkel(My3Vektor a)
	{
		return(acos(Skalarprodukt(a)/(Length()*a.Length())));
	}

My3Vektor My3Vektor::operator + (My3Vektor & v)
{
	return(Add(v));
}

My3Vektor My3Vektor::operator * (double & c)
{
	My3Vektor t;
	t.x = c*x;
	t.y = c*y;
	t.z = c*z;
	return t;
}
My3Vektor operator * (double & c, My3Vektor & v)
{
	My3Vektor t;
	t.x = c*v.X();
	t.y = c*v.Y();
	t.z = c*v.Z();
	return t;
}

bool My3Vektor::operator <= (My3Vektor & a)
{
	return(Length()<=a.Length());
}

void My3Vektor::Print()
{
	cout  << " (" << x << ", " << y << ", " << z << ")";
}

std::ostream & operator << ( std::ostream &s, My3Vektor &v)
{
	s << " (" << v.x << ", " << v.y << ", " << v.z <<")";
	return s;
}

/*
std::ostream & operator << ( std::ostream &s, My3Vektor &v)
{
	cout  << " (" << v.x << ", " << v.y << ", " << v.z <<")";
}*/

double My3Vektor::X() const {return x;}
	//double X(My3Vektor a){return a.x;};
double My3Vektor::Y(){return y;}
	//double Y(My3Vektor a){return a.y;};
double My3Vektor::Z(){return z;}
	//double Z(My3Vektor a){return a.z;};


