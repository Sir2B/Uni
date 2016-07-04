import java.util.Scanner;

/**
 * Created by Tobias on 24.02.2015.
 */
public class Fakulat {
    public static void main(String[] args){
        Scanner eingabe = new Scanner(System.in);
        System.out.print("Geben sie eine Zahl ein: ");
        int Zahl = eingabe.nextInt();
        System.out.println(Zahl +"! = " +fak(Zahl));

    }
    public static int fak(int n){
        int ergebnis = 1;
        for (int i = 2; i <= n; i++){
            ergebnis *= i;
        }
        return ergebnis;
    }
}
