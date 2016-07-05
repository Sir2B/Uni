
#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
    double d;
    cout << "Dichteverhältnis = ";
    cin >> d;

    if (d<0 || d>1)
    {
        cout << endl << "Fehler: Dichteverhältnis nicht zwischen 0 und 1!" << endl;
    }

    double x = 1.;
    for (int i=0; i<5; i++)
    {
        x = x-(x*x*x-3*x*x+4*d)/(3*x*x-6*x);
    }

    cout << endl << "Relative Eintauchtiefe x = " << x << endl;

    return 0;
}
