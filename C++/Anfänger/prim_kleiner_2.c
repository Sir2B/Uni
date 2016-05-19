//programm welches abzählt wieviel Primzahlen es gibt die kleiner sind als die eingebene Zahl

#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int testzahl, anzahl_primzahlen=0;
	cout << "Geben sie eine Zahl ein" << endl;
	cin >> testzahl;
	clock_t start = clock();
	for (int i=2; i<testzahl; i++) //
	{
		int n=0;
		for (int j=2; j<=sqrt(i); j++)
		{
			if (i%j == 0) //keine Primzahl
				{
				n++;
				break;
				}

		}
		if (n==0) //Primzahl
				{
				anzahl_primzahlen++;
				//cout << i << " Primzahl" << endl;
				}
	
	}
	
	cout << "Es gibt " << anzahl_primzahlen << " Primzahlen, die kleiner sind als "
	<< testzahl <<endl;
	clock_t end = clock();
	double zeit = (double) (end-start) / CLOCKS_PER_SEC * 1000.0;
	//double zeit = (double) difftime(end, start) *1000.0;
	cout << "Zeit: " << zeit  << " ms" <<endl;

}
