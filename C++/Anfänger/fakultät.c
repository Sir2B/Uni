#include <iostream>
using namespace std;

long lfak(long n)
{	
	long ergebnis=n;
	for(int i=n-1; i>0; i--)
	{
		ergebnis = ergebnis*i;
	}
	return ergebnis;
}


int main()
{	
	long eingabewert=0;
	cin >> eingabewert;
	cout << eingabewert << endl;
	cout << lfak(eingabewert) << endl;
	//return(0);
}
