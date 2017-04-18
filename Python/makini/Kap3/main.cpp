/*
Die Klasse StatCalc (html, source) implementiert einige grundlegende Statistikfunktionen, wie Mittelwert, Standardabweichung, ...
Ein kurzes Testprogramm ist angehängt, das Zufallszahlen in ein StatCalc Objekt füllt und anschliesend die Statistik-größen ausgibt.

(a) Probieren Sie das Programm aus und Erweitern dann die StatCalc Klasse um Methoden zur Berechnung und Ausgabe von Minimum und Maximum.
(c) In semester.dat finden Sie die Semesterzahl bis zum Physikdiplom für zufällig ausgewählte Studenten. Die ersten 100 Einträge sind von Studenten der LMU,
die restlichen 100 von Studenten der TUM. Lesen Sie die Daten ein und füllen LMU bzw TUM Zahlen jeweils in ein StatCalc Objekt. Sind die Mittelwerte im Rahmen der Schwankungen konsistent ?
(d) Überlegen Sie wie man das Problem aus (c) (mehrere Statistiken parallel führen) in einer prozeduralen Sprache (Fortran, C) angehen könnte, d.h. ohne Klassen und Objekte, nur mit Arrays und Funktionen
*/
#include <iostream>
#include "lvector3.h"

using namespace std;


int main()
 {
   lvector3 c(1.000001,1.,0.,0.);
   lvector3 d(2.,1.,1.,0.);
   lvector3 e(1.000001,-1.,0.,0.);

   cout << "angle c, e = " << c.Winkel(e) << endl; // My3Vector-Methode
   cout << "mass d = " << d.Masse() << endl; // MyLVector-Methode
   cout << "mass c = " << c.Masse() << endl; // MyLVector-Methode
   cout << "mass c+e = " << c.invMasse(e) << endl;
   cout << "Verktoraddition = " << c.Add(d) << endl;

 }
