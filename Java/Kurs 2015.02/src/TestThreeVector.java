/**
 * Created by Tobias on 25.02.2015.
 */

public class TestThreeVector {
    public static void main(String[] args) {
        ThreeVector u = new ThreeVector(1., 0.5, 2.);
        ThreeVector v = new ThreeVector(1., 2.5, -1.);
        ThreeVector w = u.Add(v);
        System.out.print("Vector w = " + w);
        ThreeVector r = u.CrossProduct(v);
        double x = w.ScalarProduct(v);
        double angle = w.Angle(u);
        System.out.println("w_x = " + w.X());
        System.out.println("angel = " + angle);

    }
}
