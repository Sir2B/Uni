#include <iostream>
#include <vector>
#include <math.h>
#include <time.h>

using namespace std;

int main()
{
	int eingabe;
	cout << "Eingabe: " << endl;
	cin >> eingabe;
	clock_t start = clock();
	int wurzl;
	vector <int> prim;

	int i, n;
	bool isprim = true;

	if (eingabe > 2)
	{
		prim.push_back(2);
	}

	if (eingabe > 3)
	{
		prim.push_back(3);
	}
	wurzl = 2; 
	i = 5; 
	while ( i < eingabe)
	{
		//wurzl = (int) sqrt(i);
		if ((wurzl + 1)*(wurzl + 1) <= i) wurzl++;

		for (n = 1; wurzl >= prim[n]; n++)
		{
			if (i%prim[n] == 0)
			{
				goto breakout;
			}
		}
		prim.push_back(i);
		
		breakout:;
		i += 2;
	}
	clock_t ende = clock();

	/*
	for (int i = 0; i < prim.size(); i++)
	{
		cout << prim[i] << endl;
	}
	*/
	


	cout << "Es sind " << prim.size() << " Primzahlen kleiner als " << eingabe << endl
		<< "Das hat " << (double) ((double) ende - (double) start) / (double) CLOCKS_PER_SEC * 1000 << " ms gedauert" << endl;
	cin >> eingabe;

	return(0);

}

