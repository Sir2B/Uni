public class Atom extends Particle {
    private String m_chemElement;
    public Atom() {}
    public Atom(double x, double y, double z, String chemElement) {
        super(x, y, z);
        this.m_chemElement = chemElement;
    }
    public String toString() {
	    String s = "Atom [" + m_chemElement + super.toString() + " ]";
	    return s;
    }
}
