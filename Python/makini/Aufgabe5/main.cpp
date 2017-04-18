/*Die Klasse StatCalc (html, source) implementiert einige grundlegende Statistikfunktionen, wie Mittelwert, Standardabweichung, ...
Ein kurzes Testprogramm ist angehängt, das Zufallszahlen in ein StatCalc Objekt füllt und anschliesend die Statistik-größen ausgibt.

(a) Probieren Sie das Programm aus und Erweitern dann die StatCalc Klasse um Methoden zur Berechnung und Ausgabe von Minimum und Maximum.
(c) In semester.dat finden Sie die Semesterzahl bis zum Physikdiplom für zufällig ausgewählte Studenten.
	Die ersten 100 Einträge sind von Studenten der LMU, die restlichen 100 von Studenten der TUM. Lesen Sie die Daten ein und füllen LMU bzw TUM Zahlen
	jeweils in ein StatCalc Objekt. Sind die Mittelwerte im Rahmen der Schwankungen konsistent ?
(d) Überlegen Sie wie man das Problem aus (c) (mehrere Statistiken parallel führen) in einer prozeduralen Sprache (Fortran, C) angehen könnte,
	d.h. ohne Klassen und Objekte, nur mit Arrays und Funktionen.
*/
#include <iostream> // pre-prozessor command
#include <cmath> // pre-prozessor command
#include <fstream>
#include "StatCalc.h"
using namespace std; // declare namespace



#include <cstdlib>
#include <time.h>

int main()
{
/* --- AUFGABE a
  StatCalc s1;  // lege StatCalc Objekt an

  srandom(time(0)); // setup random generator
  s1.initfirst();


  for ( int i=0; i<1000; i++ ) {
    double xrnd = random()*2./RAND_MAX - 1.; // Zufallszahlen zwischen [-1,1]
    s1.enter(xrnd);
  }
  */

	StatCalc TUM,LMU;
	ifstream daten ("semester.dat");
double tmp(0.);
LMU.initfirst();
TUM.initfirst();
	for (int i =0;i<100;i++)
	{
	daten >> tmp;
	LMU.enter(tmp);
	}
	for (int i =0;i<100;i++)
		{
			daten >> tmp;
		TUM.enter(tmp);
		}

  cout << LMU.getCount() << "   "
       << LMU.getMean()  << "   "
       << LMU.getStandardDeviation()  << "   "
       << LMU.getMin()  << "   "
       << LMU.getMax()  << "   "
       << endl;

  cout << TUM.getCount() << "   "
         << TUM.getMean()  << "   "
         << TUM.getStandardDeviation()  << "   "
         << TUM.getMin()  << "   "
         << TUM.getMax()  << "   "
         << endl;



  return(0);
}

