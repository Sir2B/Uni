class My3Vektor {
private:
	double x,y,z;
public:
	My3Vektor()
	{
	x=y=z=0;
	};
	My3Vektor(double a1, double a2, double a3)
	{
	x=a1;
	y=a2;
	z=a3;
	};
	
	double Length();
	
	My3Vektor Add(My3Vektor a);
	double Skalarprodukt(My3Vektor a);
	My3Vektor Vektorprodukt(My3Vektor a);
	double Winkel(My3Vektor a);

	double X(){return x;};
	double X(My3Vektor a){return a.x;};
	double Y(){return y;};
	double Y(My3Vektor a){return a.y;};
	double Z(){return z;};
	double Z(My3Vektor a){return a.z;};
};
