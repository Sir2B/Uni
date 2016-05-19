#include <iostream>
using namespace std;

class My3Vektor {
protected:
	double x,y,z;
public:
	My3Vektor();
	My3Vektor(double, double a2, double a3);
	double Length();
	My3Vektor Add(My3Vektor a);
	double Skalarprodukt(My3Vektor a);
	My3Vektor Vektorprodukt(My3Vektor a);
	double Winkel(My3Vektor a);
	My3Vektor operator + (My3Vektor & v);
	My3Vektor operator * (double & c);
	void Print();
	friend My3Vektor operator * (double & c, My3Vektor & v);
	friend std::ostream & operator << (std::ostream &s, My3Vektor &v);
	bool operator <= (My3Vektor & a);
	double X() const;
	double Y();
	double Z();
};
My3Vektor operator * (double & c, My3Vektor & v);

std::ostream & operator << (std::ostream &s, My3Vektor &v);
