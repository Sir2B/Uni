import java.util.*;

/**
 * Created by Tobias on 27.02.2015.
 */
public class testSum {
    public static int sum(int n){
        int s = 0;
        for (int i = 0; i <= n; i++){
            s += i;
        }
        return s;
    }
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int summe = sum(n);
        System.out.printf("Summe von 1 bis %d ist %d %n", n, summe);
    }
}
