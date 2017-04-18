/*
Folgen Sie jetzt der C++
Konvention das Programm
in drei verschiedene Files zu trennen:
die Deklaration der My3Vector-Klasse kommt
in eine Header-Datei (z.B. My3Vector.h), die
Implementierung der Methoden geht in ein extra
source file (z.B. My3Vector.cpp) und schliesslich
die main() Funktion zum Testen in z.B. T3Vector.cpp
*/
#include <iostream>
#include "vector3.h"

using namespace std;

 int main()
 {

    double x = 3.;
   vector3 a(1.,1.,0.);
   vector3 b(-1.,1.,0.);
   vector3 c = a + b;
   vector3 d = a * x; // von rechts
   vector3 e = x * a; // von links
   cout << c << d << e ;

 }
