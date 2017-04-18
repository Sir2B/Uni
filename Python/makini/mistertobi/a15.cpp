/*
 Zahlen einlesen und sortieren
In der Datei numbers.dat finden Sie eine Liste mit 100 Fließkommazahlen.

(a)
    Lesen die Zahlen in einen Array ein. (File-I/O in C++ siehe I/O Basics)
(b)
    Finden Sie kleinsten und größten Wert.
(c)
    Verwenden Sie die C Standardfunktion qsort
    um die Zahlen zu sortieren und sortiert auszugeben.
 */

#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	float zahlenarray [99];
	int i;
	ifstream senf("spast.dat");


	for (i=0;i<=99;i++)
	{
		senf>> zahlenarray[i];
	}

	for (i=0;i<=99;i++)
	{
		cout << zahlenarray[i] << endl;
	}


}
