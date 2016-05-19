#include "My3Vektor.h"

class MyLVektor: public My3Vektor
{
	private:
		double t;
	public:
		MyLVektor();
		MyLVektor(double, double, double, double);
		double Mass();
		double invMass(MyLVektor p);
		MyLVektor Add(MyLVektor a);
		double T();

};
