/**
 * Created by Tobias on 25.02.2015.
 */
public class ThreeVector {
    protected double x, y, z;

    public ThreeVector(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public static void main(String[] args) {
        ThreeVector u = new ThreeVector(1., 0.5, 2.);
        ThreeVector v = new ThreeVector(1., 2.5, -1.);
        ThreeVector w = u.Add(v);
        System.out.print("Vector w = " + w);
        ThreeVector r = u.CrossProduct(v);
        double x = w.ScalarProduct(v);
        double angle = w.Angle(u);
        System.out.print("w_x = " + w.X());
    }

    public double Length() {
        return (Math.sqrt(x * x + y * y + z * z));
    }

    public ThreeVector Add(ThreeVector other) {
        return new ThreeVector(this.x + other.x, this.y + other.y, this.z + other.z);
    }

    public String toString() {
        return ("(" + x + ", " + y + ", " + z + ")");
    }

    public ThreeVector CrossProduct(ThreeVector other) {
        double x = this.y * other.z - this.z * other.y;
        double y = this.z * other.x - this.x * other.z;
        double z = this.x * other.y - this.y * other.x;
        return new ThreeVector(x, y, z);
    }

    public double ScalarProduct(ThreeVector other) {
        return (this.x * other.x + this.y * other.y + this.z * other.z);
    }

    public double Angle(ThreeVector other) {
        return (Math.asin(this.ScalarProduct(other) / (this.Length() * other.Length())));
    }

    public double X() {
        return this.x;
    }

    public double Y() {
        return this.y;
    }

    public double Z() {
        return this.z;
    }
}