import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class WOLKE
{
    private NIEDERSCHLAG[]regen;
    private HAGL[]hagel;
    private int Anzahl, Anzahl2, Anzahl3, AnzahlH;
    private int Radius;
    private double xPos;
    private double yPos;
       
    
    public WOLKE(int Anzahl4, int Anzahl5, int vx)
    {
     Anzahl3=Anzahl4;
     AnzahlH=Anzahl5;
     regen = new NIEDERSCHLAG[Anzahl3];
     hagel = new HAGL[AnzahlH];
     Anzahl = 0;
       
     for (int i=0; i < Anzahl3; i++){
         double xStart = Math.round(Math.random()*500);                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
         double yStart = Math.round(Math.random()*100);
         int Rad = (int)Math.round(Math.random()*5)+5;
         regen[Anzahl]=new NIEDERSCHLAG(xStart, yStart, Rad, vx);
         Anzahl = Anzahl+1;
       
    }
    Anzahl=0;
    for (int i=0; i < AnzahlH; i++){
         double xStart = Math.round(Math.random()*500);
         double yStart = Math.round(Math.random()*100);
         int Rad = (int)Math.round(Math.random()*5)+5;
         hagel[Anzahl]=new HAGL(xStart, yStart, Rad, vx);
         Anzahl = Anzahl+1;
       
    }
    
    
}
        
    public void bewege(double zeit){
       ZEICHENFENSTER.gibFenster().loescheAlles();
       for (int i=0; i<Anzahl3; i++){
           regen[i].bewege(zeit);
           
            
       }
       for (int i=0; i<AnzahlH; i++){
            hagel[i].bewege(zeit);
        }
    } 
   
    public void vxae(int xRichtungR, int xRichtungH){
         for(int i=0; i<Anzahl3; i++){
           regen[i].vxaenderung(xRichtungR);
        }
        for(int i=0; i<AnzahlH; i++){
           hagel[i].vxaenderung(xRichtungH);
        }
    
    }
        
    
    
}
  
      
