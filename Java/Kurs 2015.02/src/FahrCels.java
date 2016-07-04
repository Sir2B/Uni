public class FahrCels {  // print Fahrenheit->Celsius Tabelle
    public static void main(String[] args) {
        double lower = 0., upper = 300., step = 20.;
        double fahr, celsius;
        fahr = lower;
        while ( fahr < upper )  {
                celsius = (5./9.) * (fahr - 32.);
                System.out.println("Fahrenheit  " + fahr +
                                   " = " + celsius +" Celsius");
                fahr += step;
        } // end-while
    }
}   // end of class FahrCels