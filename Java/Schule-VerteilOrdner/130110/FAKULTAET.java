
public class FAKULTAET
{
    // instance variables - replace the example below with your own
    private int x;

    
    public FAKULTAET()
    {
        // initialise instance variables
       
    }

    public int fakultaet(int x) {
        int y=1;
        if (y<1) {
        y=0;}
        for (int i=x; i>1; i--) {
        y=y*x;
        x--;
        }
        return y;
    }
    
}
