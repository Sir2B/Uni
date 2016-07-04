public class Nullstelle {
    // finde Nullstelle von f
    // f ist Objekt das interface Func implementiert, d.h. eine Methode double value(double) hat
    public static double find( double x1, double x2, Func f ) {

        double f1 = f.value(x1);
        double f2 = f.value(x2);
        double xn = x1;
        double fn = f1;
        for ( int i=0; i<1000 && Math.abs(fn) > 1e-6; i++ ) {  // Abbruch nach 1000 Iterationen oder bis auf 1e-6 an Nullstelle
            xn = (x1+x2)/2.;         // Neues x in Mitte
            fn = f.value(xn);        // funktionswert dazu
            if ( fn*f2 > 0. ) {      // gleiches Vorzeichen wir f2 ?
                x2 = xn;
                f2 = fn;             // dann ersetze x2,f2
            }
            else {
                x1 = xn;             // andernfalls x1,f1
                f1 = fn;
            }
            //        System.out.println(i + "Nullstelle = " + xn + "   " + fn);
        }
        return( xn );
    }
}
