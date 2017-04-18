
#include <iostream>

class vector3
{
    protected:
    double x,y,z;

    public:
     vector3();
     vector3(double a1, double a2, double a3);
    double X() const;
    double Y() const;
    double Z() const;
    double skalarprodukt( vector3 a);
    double Laenge();
    double Winkel(vector3 l2);
    vector3 Add(vector3 v);
    vector3 operator + ( vector3 & p);
    friend  vector3 operator * ( double x, vector3 & p );
    vector3 operator * ( double x);
    bool operator <= ( vector3  &p  );

};
 std::ostream & operator << (std::ostream & s , const vector3 & p);
 vector3 operator * ( double x, vector3 & p );


