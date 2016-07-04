/**
 * Created by Tobias on 23.02.2015.
 */
public class QuadratZahlen {
    public static void main(String[] args){
        int min = 1, max = 150;
        while (min <= max){
            System.out.println(min +": " +min*min +" " +min*min*min);
            min++;
        }
    }
}
