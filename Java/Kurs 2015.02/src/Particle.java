public class Particle {
    private double m_x, m_y, m_z;
    public Particle() {}
    public Particle(double x, double y, double z) {
        m_x = x;
        m_y = y;
        m_z = z;
    }
    public String toString() {
	    String s = "Particle [" + m_x + ", " + m_y + ", " + m_z + "]";
	    return s;
    }
    public void move (double dx, double dy, double dz){
        m_x += dx;
        m_y += dy;
        m_z += dz;

    }
}
