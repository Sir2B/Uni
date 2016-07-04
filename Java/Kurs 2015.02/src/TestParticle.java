import java.util.ArrayList;

public class TestParticle {
    public static void main(String[] args) {
	int n_P = 12; // Anzahl der erzeugten und beobachteten Particles 

  
	ArrayList<Particle> vecp= new ArrayList<Particle>();

	// some random nums for particles
	for (int i = 0; i < n_P; i++) {
	    Particle p;

	    double x = Math.random();
	    double y = Math.random();
	    double z = Math.random();
	    double r = Math.random();

	    if (r < 0.3) {
		    p = new Particle(x,y,z);
	    }
	    else if (r < 0.6) { 
		    p = new Atom(x,y,z, "H");
	    } 
	    else { 
            ArrayList<Atom> atoms = new ArrayList<Atom>();
            atoms.add( new Atom(x,y,z, "H"));
            atoms.add( new Atom(x,y,z, "H"));
            atoms.add( new Atom(x,y,z, "O"));
            p = new Molecule (x,y,z, atoms);
	    }
	    vecp.add( p );
	}

  
	/**** Schleife 1: ****/
	for (int i = 0; i < n_P; i++) {
	    double x = Math.random();
	    double y = Math.random();
	    double z = Math.random();
	    //*** Von der folgenden Zeile den Kommentar entfernen, um move zu testen! ***
	    vecp.get(i).move(x,y,z);
	}

	/***** Schleife 2: ****/
	for (int i = 0; i < n_P; i++) {
	    System.out.println( vecp.get(i) );
	}
    }
}
