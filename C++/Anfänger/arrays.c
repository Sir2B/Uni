#include <iostream>

using namespace std;

/*double Vektorprodukt(double vektor1[],double vektor2[])
{
	double vektor3[2];
	vektor3[0]=vektor1[1]*vektor2[2]-vektor2[2]*vektor1[1];
	vektor3[1]=vektor1[2]*vektor2[0]-vektor2[0]*vektor1[2];
	vektor3[2]=vektor1[0]*vektor2[1]-vektor2[1]*vektor1[0];
	return vektor3[1];
}*/

int main()
{
	int gesamt=0;
	double array1[] = {0.3,1.8,-2.2}, array2[] = {-2.5, 3.8, 0.4};

	for (int i=0; i<=2; i++) //Skalarprodukt ausrechnen
	{
		gesamt += array1[i]*array2[i];
	}

	double vektorprodukt[2]; //Vektorprodukt ausrechnen
	vektorprodukt[0]=array1[1]*array2[2]-array1[2]*array2[1];
	vektorprodukt[1]=array1[2]*array2[0]-array1[0]*array2[2];
	vektorprodukt[2]=array1[0]*array2[1]-array1[1]*array2[0];

	
	cout << "Skalarprodukt: " << gesamt << endl;
	cout << "Vektorprodukt: (" << vektorprodukt[0] << ", " << vektorprodukt[1] 
		<< ", " << vektorprodukt[2] << ")" << endl;
}

