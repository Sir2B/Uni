import java.util.Arrays;

/**
 * Created by Tobias on 23.02.2015.
 */
public class Fibonacci {
    public static void main(String[] args){
        //AufgabeA();
        AufgabeB();

    }
    public static long[] FibonacciFolge(long F0, long F1){
        long[] Folge = new long[100];
        Folge[0] = F0;
        Folge[1] = F1;
        for (int n = 2; n < Folge.length; n++){
            Folge[n] = Folge[n-1] + Folge[n-2];
        }
        return Folge;
    }

    public static void AufgabeA(){
        long[] Folge = FibonacciFolge(0,1);
        System.out.println(Arrays.toString(Folge));
    }
    public static void AufgabeB(){
        long[] Folge = FibonacciFolge(0,1);
        boolean Fehler = false;
        for (int n = 1; n < Folge.length-1; n++){
            if (Folge[n+1]*Folge[n-1] - Folge[n]*Folge[n] != Math.pow(-1,n)){
                Fehler = true;
            }
        }
        System.out.println("Fehler: " +Fehler);
    }
}
