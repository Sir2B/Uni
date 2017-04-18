/*
 String Klasse
Die C++ string Klasse stellt eine Vielzahl nützlicher Methoden zur Textanalyse bzw. Modifikation zur Verfügung.
In kant.txt finden Sie eine elektronische Fassung von Immanuel Kant's "Kritik der reinen Vernunft".

(a) Wieviele Zeilen enthält der Text ?

(b) Finden Sie die String Funktion die Gross-Buchstaben in Klein-Buchstaben umwandelt und transformieren sie damit den ganzen Text.

(c) Wie oft kommt das Wort Vernunft in dem Text vor ?

Hinweis: Mit getline( istream in, string s ) kann man eine ganze Zeile in einen String einlesen. Rückgabewert kann für File-Ende Test genommen werden (liefert 0).
 */

#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>

using namespace std;


int main ()
{

	string zeile;
	ifstream kant ("blabliblu.txt");
	int zeilenzahl(0);
	int anzahlvernunft(0);

	while (!kant.eof())
	{
		getline(kant, zeile);
		for (unsigned int i =0;i<zeile.size();i++)

		cout << zeile << endl;
		zeilenzahl++;
	}
	cout << zeilenzahl
		<< endl
		<<  anzahlvernunft;

}


/*
char ch;
	for (int i = 0; i <=256; i++)
	{
		ch=i;
		cout << ch << " " << i << endl;
	}
*/
