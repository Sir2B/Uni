#include <iostream>
using namespace std;

int Sum(int n)
{
	 int s=0;
	for (int i=0; i<=n; i++)
	{
		s+=i;
	}
	return s;
}

int main()
{
	cout << "Bitte Zahl eingeben: ";
	int n;
	cin >> n;
	int summe = Sum(n);
	cout << "Summe von 1 bis " << n << " ist: " << summe << endl;
}
