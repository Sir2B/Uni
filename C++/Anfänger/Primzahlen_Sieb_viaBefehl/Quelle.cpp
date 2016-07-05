#include<iostream>
#include<cmath>
#include <time.h>
#include <vector>

using namespace std;

int main(void){
	unsigned long limit;

	//cout << "Please insert upper limit.\n";
	//cin >> limit;

	clock_t start = clock();

	vector <bool> Stroke;
	unsigned long primzahlen = 0;
	Stroke.push_back(1);
	Stroke.push_back(1);
	for (unsigned long i = 2; i <= limit; ++i) Stroke.push_back(0);

	unsigned long prime = 2;
	unsigned long qprime = prime*prime;


	while (qprime <= limit)
	{
		for (unsigned i = qprime; i <= limit; i += prime){
			Stroke[i] = 1;
		}

		do ++prime; while (Stroke[prime]);
		qprime = prime*prime;
	}
	clock_t ende = clock();


	for (unsigned long i = 0; i < limit; ++i)
	{
		if (!Stroke[i]) primzahlen++;
	}

	cout << "Es sind " << primzahlen << " Primzahlen kleiner als " << limit << endl
		<< "Das hat " << (double) ((double) ende - (double) start) / (double) CLOCKS_PER_SEC * 1000 << " ms gedauert" << endl;
	cout << "Zum Beenden beliebige Zahl eingeben: ";

	//delete[] Stroke;
	int pause;
	cin >> pause;
	return 0;
}