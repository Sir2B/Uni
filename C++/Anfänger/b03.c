#include <iostream>
#include "My3Vektor.h"
using namespace std;

int main()
{
	double x = 3.;
	My3Vektor a(1.1,1.,0.), b(-1.,1.,0.);
	My3Vektor c = a + b;
	My3Vektor d = a * x;
	My3Vektor e = x * a;
	cout << "a =" << a << endl;
	cout << "b ="; b.Print(); cout << endl;
	cout << "c =" << c << endl;
	cout << "d =" << d << endl;
	cout << "e =" << e << endl;
	cout << a.X() << endl;

//Klausur
	if (a<=b)
	{
		cout << "a ist <= b" << endl;	
	}
	else
	{
		cout << "a ist nicht <= b" << endl;	
	}

	return(0);


}

