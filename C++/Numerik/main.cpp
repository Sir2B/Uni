#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main()
{
double a = 3.1, b = 3.2; //Startintervall
double Genauigkeit = 1e-10;

//Anzahl Schritte
int Anzahl = floor(log((b-a)/Genauigkeit)/log(2));
cout << Anzahl << endl << endl;

cout << setw(10) << "Schritt:" << setw(10) << "a" << setw(10) << "b" << endl;

for (int i=0; i < Anzahl; i++)
{
    cout << setw(10) << i << setw(10) << a << setw(10) << b << endl;
    //Bisektionsverfahren
    double x = (a+b)/2;
    if (sin(a)*sin(b)<0)
    {
        b = x;
    } else {
        a = x;
    }
}
cout << setw(10) << "29" << setw(10) << a << setw(10) << b << endl;

return 0;
}
