#include <iostream>

using namespace std;

double power(double x, int n)
{
	double ergebnis=1;
	for (int i=1; i<=n; i++)
	{
		ergebnis *= x;
	}
	return ergebnis;
}

int main(int argc, char** argv)
{	
	//double x;
	//int n;
	// cin >> x; cin >> n;
	cout << power(x,n) << endl;
	return(0);
}
