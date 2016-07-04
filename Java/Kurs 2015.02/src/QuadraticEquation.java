/**
 * Created by Tobias on 27.02.2015.
 */
public class QuadraticEquation {

    public static void main(String[] args) throws IllegalArgumentException{
        if (args.length != 3){
            throw new IllegalArgumentException("\n\tUsage: Java QuadraticEquation A B C \n\t e.x.: Java QuadraticEquation 2 0 0");
        }
        double[] parameter = new double[3];
        for (int i = 0; i < 3; i++){
            String arg = args[i];
            arg = arg.replace(',', '.');
            parameter[i] = Double.parseDouble(arg);
        }

//        System.out.println("test: 2,0 == 2: " +(2.0000000000000001 == 2));

        double[] x = root(parameter[0], parameter[1], parameter[2]);
        System.out.printf("Gleichung: %.2f * x^2 + %.2f * x + %.2f = 0%n", parameter[0], parameter[1], parameter[2]);
        for(double x_i: x){
            System.out.printf("x = %f%n", x_i);
        }
//        System.out.printf("Lösung: x = %f", x);
    }

    static double[] root(double A, double B, double C)
            throws IllegalArgumentException {
        // Returns the larger of the two roots of
        // the quadratic equation A*x*x + B*x + C = 0.
        // (Throws an exception if A == 0 or B*B-4*A*C < 0.)
        if (A == 0) {
            throw new IllegalArgumentException("A can't be zero.");
        }
        else {
            double disc = B*B - 4*A*C;
            if (disc < 0)
                throw new IllegalArgumentException("Discriminant < zero.");
            if (disc == 0){
                double[] Solution = new double[1];
                Solution[1] = (-B/(2*A));
                return Solution;
            }
            double[] Solutions = new double[2];
            Solutions[0] = (-B + Math.sqrt(disc)) / (2*A);
            Solutions[1] = (-B - Math.sqrt(disc)) / (2*A);
            return Solutions;
        }
    }
}
