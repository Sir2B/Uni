#include "vector3.h"

class lvector3 : public vector3
{
private:
	double t;

public:
	lvector3();
	lvector3(double c0, double c1, double c2, double c3);
	double Masse();
	double invMasse(lvector3 l2);
};
