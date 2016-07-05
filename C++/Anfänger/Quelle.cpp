#include <iostream>
#include "My3Vektor.h"
using namespace std;

int main()
{
	double x = 3.;
	My3Vektor a(1., 1., 0.), b(-1., 1., 0.);
	My3Vektor c = a + b;
	My3Vektor d = a * x;
	My3Vektor e = x * a;
	cout << "a = (" << a.X() << ", " << a.Y() << ", " << a.Z() << ")" << endl;
	cout << "b = (" << b.X() << ", " << b.Y() << ", " << b.Z() << ")" << endl;
	cout << "c = (" << c.X() << ", " << c.Y() << ", " << c.Z() << ")" << endl;
	cout << "d = (" << d.X() << ", " << d.Y() << ", " << d.Z() << ")" << endl;
	cout << "e = (" << e.X() << ", " << e.Y() << ", " << e.Z() << ")" << endl;
	cin >> x;
	return(0);

}

