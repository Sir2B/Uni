
#include "lvector3.h"
#include "cmath"


lvector3::lvector3()
{
x=y=z=t=0;
}


lvector3::lvector3(double c0, double c1, double c2, double c3)
{
x=c1;
y=c2;
z=c3;
t=c0;
}



double lvector3::Masse()
{
	return (sqrt(pow(t,2)-pow(Laenge(),2)));
}


double lvector3::invMasse(lvector3 l2)
{
	double var1;
	double var2;

	var1=pow((t+l2.t),2);
	var2=pow(Add(l2).Laenge(),2);

	return (sqrt(var1-var2));
}
