#include "Func.h"
#include <cmath>

double Func::value( double x){return 0;}


// finde Nullstelle von f nach Bisektionsverfahren
// f ist Objekt das interface Func implementiert, d.h. eine Methode double value(double) hat
double  Nullstelle::find( double x1, double x2, Func &f ) {
    double f1 = f.value(x1);
    double f2 = f.value(x2);
    double xn = x1;
    double fn = f1;
    for ( int i=0; i<1000 && fabs(fn) > 1e-6; i++ ) {  // Abbruch nach 1000 Iterationen oder bis auf 1e-6 an Nullstelle
      xn = (x1+x2)/2.;         // Neues x in Mitte
      fn = f.value(xn);        // Funktionswert dazu
      if ( fn*f2 > 0. ) {      // gleiches Vorzeichen wir f2 ?
    x2 = xn;
    f2 = fn;             // dann ersetze x2,f2
      }
      else {
    x1 = xn;             // andernfalls x1,f1
    f1 = fn;
      }
    }
    return( xn );
  }

