/**
 * Created by Tobias on 23.02.2015.
 */
public class IntegerZahlen {
    public static void main(String[] args){
        //AufgabeA();
        //AufgabeB();
        AufgabeD();
    }
    public static void AufgabeA(){
        for (int i = -16; i <= 16; i++){
            System.out.println(i +" " +Integer.toHexString(i) +" " +Integer.toBinaryString(i));
        }
    }
    public static void AufgabeB(){
        for (double d = -4.; d <= 4.1; d++){
            double p = Math.pow(2., d);
            System.out.println(p +" " +
                               Long.toHexString(Double.doubleToLongBits(p)) +" " +
                               Long.toBinaryString(Double.doubleToLongBits(p)) );
        }
    }
    public static void AufgabeD(){
        int counter = 0;
        float eps = 1.f, onePlusEps = 0;
        while(onePlusEps != 1.0){
            eps /= 2.;
            onePlusEps = 1.0f + eps;
            counter++;
        }
        System.out.println(counter);
    }
}
