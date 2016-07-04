/**
 * Created by Tobias on 25.02.2015.
 */
public class TestComplex {
    public static void main(String[] args) {

        Complex a = new Complex( 1., 0.5);
        Complex b = new Complex( 1., -2.5);
        Complex e = a.clone();
        a = a.Add(b);
        System.out.println(b.Mult(5));
        Complex d = b.Mult(a);

        System.out.println("Komplexe Zahl e = " + e );
        if ( a.equals(e)){
            System.out.println("Fehler");
        }
        Double x = d.getRad();
        Double phi = d.getExp();

    }
}