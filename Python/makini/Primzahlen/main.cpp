#include <iostream>
#include <vector>
#include <cmath>


using namespace std;

int main()
{
	int eingabe;
	cout << "Eingabe: " << endl;
	cin >> eingabe;
	clock_t start = clock();
	double wurzl;
	vector <int> prim;

	int i,n;
	bool isprim=true;

	if (eingabe>2)
	{
		prim.push_back(2);
	}
	else
		isprim=false;
	for (i=3;i<eingabe;i+=2)
	{
		wurzl = sqrt(i);
		for (n=0;n<prim.size() && wurzl>=prim[n];n++)
		{
			if(i%prim[n]== 0)
			{
				isprim=false;
				break;
			}
		}
		if (isprim)
		{
			prim.push_back(i);
		}
		else
			isprim = true;
	}
	clock_t ende = clock();

	cout << "Es sind " << prim.size() << " Primzahlen kleiner als " << eingabe << endl
			<< "Das hat " << (double)((double)ende-(double)start)/ (double)CLOCKS_PER_SEC * 1000 << " ms gedauert" << endl;
}
