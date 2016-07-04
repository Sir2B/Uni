/**
 * Created by Tobias on 26.02.2015.
 */
public class Simpson implements Integral{
    int Intervalls;
    public Simpson(){
        Intervalls = 1;
    }
    public Simpson(int number){
        Intervalls = number;
    }
    public double calc(double x1, double x2, Func f){
        double sum = 0;
        double length = (x2-x1)/ Intervalls;
        for (double i = 0; i < Intervalls; i++){
            double current_x1 = x1 + i*length;
            double current_x2 = x1 + (i+1)*length;
            sum += (length)/6 * (f.value(current_x1) + 4*f.value((current_x1+current_x2)/2) + f.value(current_x2));
        }
        return sum;
    }
}
