import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class NIEDERSCHLAG
{
    private int Radius;
    private double xPos;
    private double yPos;
    private double vx;
    private double vy;
    
    public NIEDERSCHLAG(double xStart, double yStart, int RadiusStart, int vxi)
    {
        vx=vxi;
        xPos=xStart;
        yPos=yStart;
        Radius=RadiusStart;
        zeichne();
        vy=10;
        
        
    }
    
    public void zeichne() {
    ZEICHENFENSTER.gibFenster().zeichneKreis((int)xPos,(int)yPos,Radius);
    
    }
    public void bewege(double zeit) {
    
        
        xPos=xPos+vx*zeit+(Math.random());
        yPos=yPos+vy*zeit+(Math.random());
        ZEICHENFENSTER.gibFenster().zeichneKreis((int)xPos,(int)yPos,Radius);
        if (yPos>500) {
            yPos=0.00;
        }
        if (xPos>600) {
            xPos=0.00;
        }
        if (xPos<0) {
            xPos=600;
        }
     
    
    }
    
    public void vxaenderung(int vxi){
       vx=vxi;
    
    }

}
