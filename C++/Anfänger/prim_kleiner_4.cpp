//programm welches abzählt wieviel Primzahlen es gibt die kleiner sind als die eingebene Zahl

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

//void primzahlen

int main()
{
	int testzahl;
	cin >> testzahl;
	clock_t start = clock();
	vector <int> prim;
	cout << "Geben sie eine Zahl ein" << endl;
	if (testzahl >2)
	{
		prim.push_back(2);
	}

	for (int i=3; i<testzahl; i+=2) //
	{
		bool n=true;
		int e= (int)sqrt(i);
		for (int j=0; j<prim.size() &&prim[j]<=e; j++)
		{
			if (i%prim[j] == 0) //keine Primzahl
				{
				n=false;
				break;
				}

		}
		if (n==true) //Primzahl
				{
				prim.push_back(i);
				//cout << i << " Primzahl" << endl;
				}
	
	}
	
	cout << "Es gibt " << prim.size() << " Primzahlen, die kleiner sind als "
	<< testzahl <<endl;
	clock_t end = clock();
	double zeit = (double) (end-start) / CLOCKS_PER_SEC * 1000.0;
	//double zeit = (double) difftime(end, start) *1000.0;
	cout << "Zeit: " << zeit  << " ms" <<endl;

}
