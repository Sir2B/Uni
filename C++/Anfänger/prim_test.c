#include <iostream>
#include <cmath>
using namespace std;

int main()
{
int testzahl, n;
cout << "Geben die eine Zahl ein" << endl;
cin >> testzahl;

for (int i=2; i<testzahl; i++)
{
	if (testzahl%i == 0)
	{
		n++;
		cout << "Zahl ist durch " << i << " teilbar" << endl; 
	}
}

if (n==0)
{
	cout << "Zahl ist eine Primzahl" << endl;
}
}
