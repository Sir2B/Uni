#include "vector3.h"
#include <math.h>
#include <iostream>


vector3::vector3()
    {
        x=y=z=0;
    }
vector3::vector3(double a1, double a2, double a3)
    {
        x=a1;
        y=a2;
        z=a3;
    }
double vector3::X()
        {
            return x;
        }
double vector3::Y()
        {
            return y;
        }
double vector3::Z()
        {
            return z;
        }
double vector3::skalarprodukt( vector3 a)
        {
            double skalar;
            skalar = a.x*x + a.y*y + a.z*z;
            return skalar;
        }
double vector3::Laenge()
        {
            double l;
            l = sqrt(x*x + y*y + z*z);
            return l;
        }
vector3 vector3::Add (vector3 v)
        {
            v.x = x+v.x;
            v.y = y+v.y;
            v.z = z+v.z;
            return v;
        }

vector3 vector3::operator + ( vector3 & a)
        {
            vector3 c;
            c.x = a.x+x;
            c.y = a.y+y;
            c.z = a.z+z;
            //std::cout << "tobi duftet";
            return c;
        }
vector3 vector3::operator * ( double s)
    {
        vector3 d;
        d.x = x*s;
        d.y = y*s;
        d.z = z*s;
        return d;
    }
vector3 operator * ( double x, vector3 & p )
    {
        vector3 e;
        e.x = p.x*x;
        e.y = p.y*x;
        e.z = p.z*x;
        return e;
    }
std::ostream & operator << (std::ostream & s , const vector3 & p)
    {
        s << p.x << " " << p.y << " " << p.z << std::endl;
        return s;
    }

