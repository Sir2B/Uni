import java.util.Arrays;
import java.util.Scanner;

/**
 * Created by Tobias on 23.02.2015.
 */
public class Primzahlen {
    public static void main(String[] args){
        Scanner eingabe = new Scanner(System.in);
        System.out.print("maxNumber: ");
        int maxNumber = eingabe.nextInt();
        //printPrims(100);
        AufgabeB(maxNumber);
        AufgabeC(maxNumber);
    }
    public static void printPrims(int maxNumber){
        for (int i = 2; i < maxNumber; i++){
            if(IsPrim(i)){
                System.out.println(i);
            }
        }
    }

    public static boolean IsPrim(int Zahl){
        if (Zahl < 2) return false;
        int max = (int)(Math.sqrt(Zahl) + 1.5d);
        for (int n = 2; n < max; n++){
            if(Zahl%n==0) return false;
        }
        return true;
    }
    public static void AufgabeB(int maxNumber){
        long StartTime = System.currentTimeMillis();
        //int maxNumber = 1000000;
        int counter = 0;
        if (maxNumber>2) counter++;
        for (int i = 3; i < maxNumber; i+=2){
            if(IsPrim(i)) counter++;
        }
        System.out.println("Es gibt " + counter + " Primzahlen, die kleiner sind als " + maxNumber);
        System.out.println("Zeit: " + (System.currentTimeMillis() - StartTime) + " ms");
    }
    public static void AufgabeC(int maxNumber){
        System.out.println("Sieb des Eratosthenes:");
        long StartTime = System.currentTimeMillis();
        //int maxNumber = 100;

        boolean[] Prim = new boolean[maxNumber];
        Arrays.fill(Prim, Boolean.TRUE);
        Prim[0] = false;
        Prim[1] = false;

        for (int i = 2; i < maxNumber; i++){
            if (Prim[i]) {
                int untilNumber = (int)(maxNumber-1)/i;
                for (int n = 2; n <= untilNumber; n++){
                    Prim[i*n] = false;
                }
            }
        }
        //System.out.println(Arrays.toString(Prim));
        int counter = 0;
        for (int i = 0; i < maxNumber; i++){
            if (Prim[i]){
                counter++;
                //System.out.print(i +", ");
            }
        }
        System.out.println("Es gibt " + counter + " Primzahlen, die kleiner sind als " + maxNumber);
        System.out.println("Sieb Zeit: " + (System.currentTimeMillis() - StartTime) + " ms");
    }
}
