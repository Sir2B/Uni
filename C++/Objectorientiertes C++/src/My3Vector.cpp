#include "My3Vector.h"
#include <math.h>
using namespace std;

My3Vector::My3Vector()
{
    //ctor
    x = 0.;
    y = 0.;
    z = 0.; // set coords to 0.
}

My3Vector::~My3Vector()
{
    //dtor
}

My3Vector::My3Vector( double c1, double c2, double c3 )
{
    x = c1;
    y = c2;
    z = c3; // take args for coords
}
// get length of vector
double My3Vector::Length()
{
    return( sqrt( x*x + y*y +z*z ) );
}
// access elements
double My3Vector::X()
{
    return x;
}
double My3Vector::Y()
{
    return y;
}
double My3Vector::Z()
{
    return z;
}
// add
My3Vector My3Vector::Add(const My3Vector & p ) const
{
    My3Vector t;
    t.x = x + p.x;
    t.y = y + p.y;
    t.z = z + p.z;
    return( t );
}

void My3Vector::Print() const
{
    cout << "( " << x << ", " << y << ", " << z << " )" << endl;
}

My3Vector My3Vector::operator + (const My3Vector & xv ) const
{
  My3Vector tv;
  tv.x = x + xv.x;
  tv.y = y + xv.y;
  tv.z = z + xv.z;
  return tv;
}

// multplikation von rechts
My3Vector My3Vector::operator * (const double & c ) const
{
  My3Vector tv;
  tv.x = x * c;
  tv.y = y * c;
  tv.z = z * c;
  return tv;
}
// multplikation von links
My3Vector operator * (const double & c, const My3Vector & v )
{
  return( v * c );
}
ostream & operator << ( ostream &s, const My3Vector &v)
{
  s << "(" << v.x <<","<< v.y <<","<< v.z <<")";
  return s;
}
