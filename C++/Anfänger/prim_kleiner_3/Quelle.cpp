//programm welches abzählt wieviel Primzahlen es gibt die kleiner sind als die eingebene Zahl

#include <iostream>
#include <cmath>
#include <ctime>

using namespace std;

//void primzahlen

int main()
{
	int testzahl, anzahl_primzahlen = 0;
	cout << "Geben sie eine Zahl ein" << endl;
	cin >> testzahl;
	clock_t start = clock();
	if (testzahl>2)
	{
		anzahl_primzahlen++;
	}
	for (int i = 3; i<testzahl; i += 2) //
	{
		bool n = true;
		double wrz = sqrt(i);
		for (int j = 2; j <=wrz ; j++)
		{
			if (i%j == 0) //keine Primzahl
			{
				n = false;
				break;
			}

		}
		if (n == true) //Primzahl
		{
			anzahl_primzahlen++;
			//cout << i << " Primzahl" << endl;
		}

	}

	cout << "Es gibt " << anzahl_primzahlen << " Primzahlen, die kleiner sind als "
		<< testzahl << endl;
	clock_t end = clock();
	double zeit = (double) (end - start) / CLOCKS_PER_SEC * 1000.0;
	//double zeit = (double) difftime(end, start) *1000.0;
	cout << "Zeit: " << zeit << " ms" << endl;
	cin>>testzahl;
}
