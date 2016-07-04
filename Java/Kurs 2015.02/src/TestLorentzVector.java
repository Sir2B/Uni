/**
 * Created by Tobias on 26.02.2015.
 */
public class TestLorentzVector {
    public static void main(String[] args){
        LorentzVector a = new LorentzVector(45.0002,0.,0.,45.0);
        LorentzVector b = new LorentzVector(45.0002,31.8198,0.,31.8198);
        System.out.println("Angle = " + a.Angle(b));
        System.out.println("Mass a = " + a.Mass());
        System.out.println("Mass b = " + b.Mass());
        System.out.println("Mass a+b = " + b.InvMass(a));
    }
}
