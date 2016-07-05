#include<iostream>
#include<cmath>
#include<time.h>
using namespace std;

int main(void){
	unsigned limit;

	cout << "Eingabe: " << endl;
	cin >> limit;
	clock_t start = clock();
	bool *Stroke = new bool[limit + 1];
	Stroke[0] = 1;
	Stroke[1] = 1;
	for (unsigned i = 2; i <= limit; ++i) Stroke[i] = 0;

	unsigned prime = 2;
	while (pow((double) prime, 2.0) <= limit){
		for (unsigned i = (int) pow((double) prime, 2.0); i <= limit; i += prime){
			Stroke[i] = 1;
		}

		do ++prime; while (Stroke[prime]);
	}
	int a = 0;
	//cout << "\nPrimes less or equal " << limit << " are:\n";
	for (unsigned i = 0; i <= limit; ++i){
		if (!Stroke[i]) a++;//cout << i << endl;
	}
	delete[] Stroke;
	cout << "Es sind " << a << " Primzahlen kleiner als " << limit << endl;
	clock_t end = clock();
	double zeit = (double) (end - start) / CLOCKS_PER_SEC * 1000.0;
	cout << "Zeit: " << zeit << " ms" << endl;
	cin >> limit;
	return 0;
}