#include <iostream>
#include "My3Vektor.h"
using namespace std;

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

