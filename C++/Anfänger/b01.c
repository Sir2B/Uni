#include <iostream>
#include <cmath>
using namespace std;

class My3Vektor {
private:
	double x,y,z;
public:
	My3Vektor()
	{
	x=y=z=0;
	};
	My3Vektor(double a1, double a2, double a3)
	{
	x=a1;
	y=a2;
	z=a3;
	};
	
	double Length()
	{
		return(sqrt(x*x+y*y+z*z));
	};
	
	My3Vektor Add(My3Vektor a)
	{
		My3Vektor t;
		t.x = x +a.x;
		t.y = y +a.y;
		t.z = z +a.z;
		return(t);
	};
	double Skalarprodukt(My3Vektor a)
	{
		return(x*a.x+y*a.y+z*a.z);
	};
	My3Vektor Vektorprodukt(My3Vektor a)
	{
		My3Vektor t;
		t.x = a.y*z-a.z*y;
		t.y = a.z*x-a.x*z;
		t.z = a.x*y-a.y*x;
		return(t);
	};
	double Winkel(My3Vektor a)
	{
		return(acos(Skalarprodukt(a)/(Length()*a.Length())));
	};
	double X(){return x;};
	double X(My3Vektor a){return a.x;};
	double Y(){return y;};
	double Y(My3Vektor a){return a.y;};
	double Z(){return z;};
	double Z(My3Vektor a){return a.z;};
};

int main()
{
	My3Vektor a, b(1.,1.,-1.), c(0.,2.,1.);
	a = b.Add(c);
	cout << "a = (" << a.X() <<", " << a.Y() <<", " <<a.Z()<<")" <<endl;
	cout << "Länge a= "<< a.Length() << endl;
	cout << "Skalarprodukt von a mit b: "<<a.Skalarprodukt(b) << endl;
	cout << "Vektorprodukt von a mit b: ("<<a.Vektorprodukt(b).X()<<", "<<
	a.Vektorprodukt(b).Y()<< ", " << a.Vektorprodukt(b).Z()<<")"<<endl;
	cout << "Winkel zwischen a mit b: "<<a.Winkel(b) << endl;

	double winkel = a.Winkel(b);
	return(0);
}
