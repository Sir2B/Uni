#include <iostream>

using namespace std;

int main() 
{
    int b = 42;
    int *pb;  // pb deklariert als pointer auf int
    pb = &b;  // & ist Adress operator, liefert Adresse von b
    cout << b << endl;
    cout << pb << endl; // Kryptische Adresse
    cout << *pb << endl; // De-referenzieren: *pb == b
    double x = 7.256;
    double *px = &x; // px deklariert als pointer auf double
    //px = &b; // illegal pointer auf double kann nicht Adresse von int nehmen

    return(0);
}
