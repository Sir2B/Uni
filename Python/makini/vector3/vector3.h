#ifndef VECTOR3
#define VECTOR3
#include <iostream>

class vector3
{
    public:
    double x,y,z;

    public:
     vector3();
     vector3(double a1, double a2, double a3);
    double X();
    double Y();
    double Z();
    double skalarprodukt( vector3 a);
    double Laenge();
    vector3 Add(vector3 v);
    vector3 operator + ( vector3 & p);
    friend  vector3 operator * ( double x, vector3 & p );
    vector3 operator * ( double x);

};
 std::ostream & operator << (std::ostream & s , const vector3 & p);
 vector3 operator * ( double x, vector3 & p );
#endif // VECTOR3

