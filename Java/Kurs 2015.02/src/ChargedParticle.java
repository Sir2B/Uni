public class ChargedParticle extends Particle {
    private double m_charge;
    public ChargedParticle() {}
    public ChargedParticle(double x, double y, double z, double charge) {
        super(x,y,z);
        m_charge = charge;

    }
    public String toString() {  // convert to string
        String s = "ChargedParticle [" + m_charge + " e " +  super.toString() + "]";
        return s;
    }
}
