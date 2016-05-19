#include <iostream>
#include <cmath>
#include "Func.h"

using namespace std;

class TFunc1 : public Func   // concrete class 1
{
public:
    double value( double x)   // define method
    {
        return( cos(x) -x);
    }
};
class TFunc2 : public Func   // concrete class 2
{
public:
    double value( double x)   // define method
    {
        return( exp(x) -x);
    }
};
class TFunc3 : public Func   // concrete class 2
{
public:
    double value( double x)   // define method
    {
        return( sin(x)-0.01);
    }
};
class TFuncGravity : public Func   // concrete class 2
{
public:
    double value( double alpha)   // define method
    {
        double height = 0.;
        double velocity = 10;
        double GRAVITY = 9.81;

        double a = velocity*velocity/(2.0*GRAVITY);
        double b = (2*GRAVITY*height)/(velocity*velocity);

        return(b*cos(2*alpha)*(1/(sqrt(a*pow(sin(alpha),-2.0)+1))+1));
    }
};

int main()
{
    double x1 = 0.1, x2 = M_PI_4; // Startintervall
    TFunc1 t1;
    TFunc2 t2;
    TFunc3 t3;
    TFuncGravity t4;
    Nullstelle ns;
    cout << "Nullstelle = " << ns.find( x1, x2, t1 ) << endl;
    cout << "Nullstelle = " << ns.find( x1, x2, t2 ) << endl;
    cout << "Nullstelle = " << ns.find( x1, x2, t3 ) << endl;
    cout << "\nSchiefer Wurf: " << (ns.find( x1, x2, t4 ))*360/(2*M_PI) << endl;
}
