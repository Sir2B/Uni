
/**
 * Created by Tobias on 26.02.2015.
 */
public class LorentzVector extends ThreeVector {
    private double t;

    public LorentzVector(double t, double x, double y, double z){
        super(x,y,z);
        this.t = t;
    }

    public double Mass(){
        return Math.sqrt(t*t-x*x-y*y-z*z);
    }

    public double InvMass(LorentzVector other){
        return this.Add(other).Mass();
    }

    public LorentzVector Add (LorentzVector other){
        return new LorentzVector(t+other.t, x+other.x, y+other.y, z+other.z);
    }

    public double T(){
        return t;
    }

}
