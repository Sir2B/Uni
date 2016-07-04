/**
 * Created by Tobias on 23.02.2015.
 */
public class Identity {
    public static void main(String[] args){
        boolean error = false;
        for (int n = 1; n <= 200; n++){
            int FirstSum = 0, SecondSum = 0;
            for (int i = 1; i <= n; i++) {
                FirstSum += i * i * i;
                SecondSum += i;
            }
            SecondSum *= SecondSum;
            System.out.println(FirstSum +" = " +SecondSum);
            if (FirstSum != SecondSum) error = true;
        }
        System.out.println("Fehler: " +error);
    }
}
