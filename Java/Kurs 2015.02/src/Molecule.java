import java.util.ArrayList;

public class Molecule extends Particle {
    private ArrayList<Atom> m_atoms = new ArrayList<Atom>();
    public Molecule() {}
    Molecule(double x, double y, double z, ArrayList<Atom> atoms) {
        super(x, y, z);
        m_atoms = atoms;
    }
    public String toString() {  // convert to string
        String s = "Molecule ( " ;
        for (int i = 0; i < m_atoms.size(); i++) {
            s +=  m_atoms.get(i).toString() + " ";
        }
        s+=  " )";
        return s;
    }
}
