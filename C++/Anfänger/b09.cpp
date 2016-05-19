#include <iostream>
#include "MyLVektor.h"

using namespace std;

int main()
{
	MyLVektor a(1.,0.,1.,0.), b(2.,0.,0.,-1.);
	MyLVektor c(1.000001,1.,0.,0.);
   	MyLVektor d(2.,1.,1.,0.);
   	MyLVektor e(1.000001,-1.,0.,0.);

	cout << a.Winkel(b) <<endl;
	cout << a.Add(b).T() <<endl<<a.Add(b).X() << endl;
	cout << c.Mass() << endl;
	cout << c.invMass(e) << endl;
	
}
