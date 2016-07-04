import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class KREIS
{
    public int xPos,yPos,radius,zeit;
    private JButton taste1, taste2;

    public KREIS()
    {
       xPos = 250; 
       yPos = 250;
       radius = 5;
       zeichne();
       taste1 = new JButton("loeschen");
       taste2 = new JButton("Haus vom Nikolaus");
       
       taste1.addActionListener(new ActionListener()
        { public void actionPerformed(ActionEvent e) {
            loesche();
                }});
                
       taste2.addActionListener(new ActionListener()
        { public void actionPerformed(ActionEvent e) {
            haus_vom_nikolaus();
                }});
                
      
    }
    
    

    public void zeichne() {
    ZEICHENFENSTER.gibFenster().zeichneKreis(xPos,yPos,radius);
    }
    
    public void loesche() {
    ZEICHENFENSTER.gibFenster().loescheAlles();
    zeichne();
    }
    
    public void loeschekreis(int x, int y) {
    ZEICHENFENSTER.gibFenster().loescheKreis(xPos,yPos,radius);
    }

    public void rechts(int weite) {
       for (int i=0; i<weite; i++) {
        ZEICHENFENSTER.gibFenster().loescheAlles();
        xPos++;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
    }
    
    public void links(int weite) {
       for (int i=0; i<weite; i++) {
        ZEICHENFENSTER.gibFenster().loescheAlles();
        xPos--;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
    }
    
    public void horizontal(int weite) {
       if (weite>0) {
        rechts(weite);
    } else {
       links(-weite);
    }
    }
    
    public void vertikal(int weite) {
       if (weite>0) {
        runter(weite);
    } else {
       hoch(-weite);
    }
    }
    
    public void runter(int weite) {
    for (int i=0;i<weite;i++) {
      ZEICHENFENSTER.gibFenster().loescheAlles();
      yPos++;
      zeichne();
      ZEICHENFENSTER.gibFenster().warte(25);
      }
    }
    
    public void hoch(int weite) {
    for (int i=0;i<weite;i++) {
      ZEICHENFENSTER.gibFenster().loescheAlles();
      yPos--;
      zeichne();
      ZEICHENFENSTER.gibFenster().warte(25);
      }
    }
    
    public void rechtsunten(int weite) {
    for (int i=0;i<weite;i++) {
      ZEICHENFENSTER.gibFenster().loescheAlles();
      yPos++;
      xPos++;
      zeichne();
      ZEICHENFENSTER.gibFenster().warte(25);
      }
    }
    
    public void rechtsoben(int weite) {
    for (int i=0;i<weite;i++) {
      ZEICHENFENSTER.gibFenster().loescheAlles();
      yPos--;
      xPos++;
      zeichne();
      ZEICHENFENSTER.gibFenster().warte(25);
      }
    }
    
    public void linksunten(int weite) {
    for (int i=0;i<weite;i++) {
      ZEICHENFENSTER.gibFenster().loescheAlles();
      yPos++;
      xPos--;
      zeichne();
      ZEICHENFENSTER.gibFenster().warte(25);
      }
    }
    
    public void linksoben(int weite) {
    for (int i=0;i<weite;i++) {
      ZEICHENFENSTER.gibFenster().loescheAlles();
      yPos--;
      xPos--;
      zeichne();
      ZEICHENFENSTER.gibFenster().warte(25);
      }
    }
    
    public void schraeg(int dx, int dy) {
     if (dx==0) {
      if (dy>0) {
       for (int i=0;i<dy;i++) {
        yPos++;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
       }
      }else{
       for (int i=0;i<Math.abs(dy);i++) {
        yPos--;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
       }
      }
     }else{
      if (dx>0) {
       if (dy>0) {
        if (dx>dy) {
        int a = (int)Math.round(dx/dy); 
        for (int i=0;i<dy;i++) {
        yPos++;
        xPos = xPos + a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        
        }else{
        int a = (int)Math.round(dy/dx); 
        for (int i=0;i<dx;i++) {
        xPos++;
        yPos = yPos + a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        }
       }else{
        dy=-dy;
        if (dx>dy) {
        int a = (int)Math.round(dx/dy); 
        for (int i=0;i<dy;i++) {
        yPos--;
        xPos = xPos + a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        
        }else{
        int a = (int)Math.round(dy/dx); 
        for (int i=0;i<dx;i++) {
        xPos++;
        yPos = yPos - a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        }
       }
      }else{
       if (dy>0) {
           dx=-dx;
        if (dx>dy) {
        int a = (int)Math.round(dx/dy); 
        for (int i=0;i<dy;i++) {
        yPos++;
        xPos = xPos - a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        
        }else{
        int a = (int)Math.round(dy/dx); 
        for (int i=0;i<dx;i++) {
        xPos--;
        yPos = yPos + a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        }
       }else{
         dx=-dx;
         dy=-dy;
        if (dx>dy) {
        int a = (int)Math.round(dx/dy); 
        for (int i=0;i<dy;i++) {
        yPos--;
        xPos = xPos - a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        
        }else{
        int a = (int)Math.round(dy/dx); 
        for (int i=0;i<dx;i++) {
        xPos--;
        yPos = yPos - a;
        zeichne();
        ZEICHENFENSTER.gibFenster().warte(25);
        }
        }
       }
      }
     }
    }
    
    public void abc(int x) {
        for (int i=0;i<x;i++) {
    schraeg(70,200);
    schraeg(200,70);
    schraeg(-70,-200);
    schraeg(-200,-70);
    ZEICHENFENSTER.gibFenster().loescheAlles();
}
    }
    
    public void korrdinaten(int x, int y) {
       
       xPos=x;
       yPos=y;
       ZEICHENFENSTER.gibFenster().loescheAlles();
       zeichne();
       
    }
    
   
    public void haus_vom_nikolaus() {
        
    rechtsoben(50);
    links(50);
    rechtsunten(50);
    links(50);
    hoch(50);
    rechtsoben(25);
    rechtsunten(25);
    runter(50);
    
    }
    public void kreis(double r){
        
       int ry = (int)Math.round(Math.sqrt(r));
       
      }
      
      
    public void ping(int anzahl){
        int hoehe = 500-yPos;
     for (int i=0; i<anzahl; i++) {
        for (int e=0; e<hoehe; e++) {
         ZEICHENFENSTER.gibFenster().loescheAlles();
         
         yPos++;
         zeichne();
         ZEICHENFENSTER.gibFenster().warte(5);
        }
        for (int e=0; e<hoehe; e++) {
         ZEICHENFENSTER.gibFenster().loescheAlles();
         yPos--;
         zeichne();
         ZEICHENFENSTER.gibFenster().warte(5);
        }
        }
    }
    
    public void ping2(int anzahl){
        int hoehe = 500-yPos;
     for (int i=0; i<anzahl; i++) {
        for (int e=0; e<hoehe; e++) {
         
         zeit++;
         ZEICHENFENSTER.gibFenster().loescheAlles();
         
         yPos=hoehe+(zeit^2);
         zeichne();
         ZEICHENFENSTER.gibFenster().warte(5);
        }
        for (int e=0; e<hoehe; e++) {
            zeit--;
         ZEICHENFENSTER.gibFenster().loescheAlles();
         yPos=hoehe+(zeit^2);
         zeichne();
         ZEICHENFENSTER.gibFenster().warte(5);
        }
        }
    }
    
    public void bedingung() {}
    

   //public void bewegeRechtsmitStrich(int weite) {
    //    int xanfang = xPos;
    //    int xende = xanfang;
     //  for (int i=0; i<weite; i++) {
     //  loeschekreis(50, 50);
     //   xPos++;
     //   xende++;
      //  zeichne();
      //  ZEICHENFENSTER.gibFenster().zeichneStrecke(xanfang, yPos, xende, yPos);
      //  ZEICHENFENSTER.gibFenster().warte(25);
      //         
      //  }
   //}
    
    
    
}
