/**
 * Created by Tobias on 26.02.2015.
 */
public class TestIntegral {
    public static void main(String[] args){
        double x1 = 0., x2 = Math.PI/2; // Startintervall
        Integral MyIntegral = new Trapez(10000);
        Integral MyIntegral2 = new Simpson(10000);
        System.out.println("Integral = " + MyIntegral.calc(x1, x2, new TFunc3()));
        System.out.println("Integral = " + MyIntegral2.calc(x1, x2, new TFunc3()));
        System.out.println(Math.sin(0) +", " +Math.sin(Math.PI/2));


    }
}
