import java.util.Arrays;

/**
 * Created by Tobias on 24.02.2015.
 */
public class LinAlgebra {
    public static void main(String[] args){
        AufgabeA();
    }
    public static void AufgabeA(){
        double Array1[] = {0.3, 1.8, -2.2};
        double Array2[] = {-2.5, 3.8, 0.4};
        System.out.println(Skalarproduct(Array1,Array2));
        System.out.println(Arrays.toString(Vectorproduct(Array1, Array2)));

    }
    public static double Skalarproduct(double[] Vect1, double[] Vect2){
        double Ergebnis = 0;
        for (int i = 0; i < Vect1.length; i++){
            Ergebnis += Vect1[i] * Vect2[i];
        }
        return Ergebnis;
    }
    public static double[] Vectorproduct(double[] Vect1, double[] Vect2){
        double[] Ergebnis = new double[3];
        Ergebnis[0] = Vect1[1] * Vect2[2] - Vect1[2] * Vect2[1];
        Ergebnis[1] = Vect1[2] * Vect2[0] - Vect1[0] * Vect2[2];
        Ergebnis[2] = Vect1[0] * Vect2[1] - Vect1[1] * Vect2[0];
        return Ergebnis;

    }
}
