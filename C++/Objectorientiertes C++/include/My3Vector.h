#ifndef MY3VECTOR_H
#define MY3VECTOR_H

#include <iostream>


class My3Vector
{
private:
    double x;
    double y;
    double z;
public:
    My3Vector();
    My3Vector(double c1, double c2, double c3);
    virtual ~My3Vector();
    double Length();
    double X();
    double Y();
    double Z();
    My3Vector Add(const My3Vector & p) const;
    double Dot(const My3Vector & x) const;
    double Angle(const My3Vector & x) const;
    void Print() const;

    My3Vector operator + (const My3Vector & xv ) const;
    My3Vector operator * (const double & c ) const;
    friend std::ostream & operator << ( std::ostream &s, const My3Vector &x);

protected:
private:
};

My3Vector operator * (const double & c, const My3Vector & v );

#endif // MY3VECTOR_H
