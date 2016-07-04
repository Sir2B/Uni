import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.Timer;


public class JESUS_CHRIST_SUPERSTAR
{
    private WOLKE wolke;
    private double vx;
    private double vy;
    private int startstop, anzahlH, anzahlR;
    private Timer uhr;
    private JButton StopIt;    
    
    
    public JESUS_CHRIST_SUPERSTAR()
    {
        startstop=0;
        uhr= new Timer(10, new ActionListener(){
            public void actionPerformed(ActionEvent e)
            { wolke.bewege(0.1);}
        });
        
        StopIt = new JButton("Stop");
        StopIt.addActionListener(new ActionListener()
            {public void actionPerformed(ActionEvent e)
               {
                   if (startstop == 0) {
                       uhr.stop();
                       StopIt.setText("Start");
                       startstop=1;
                    }
                   else if (startstop == 1) {
                       uhr.start();
                       StopIt.setText("Stop");
                       startstop=0;
                    }
                
               }
        });
    ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(StopIt, "unten");
    
       gib_moi_mehra_rengdropfa_her(50,20,10);
       uhr.start();
    }
    
      
    public void startit_du_nulla(){
        uhr.start();
    }
    
    public void stopitnow(){
        uhr.stop();
    
    }
    public void geschwindigkeit(int xRichtungR, int xRichtungH){
        
           wolke.vxae(xRichtungR, xRichtungH);
        
        
    }
    public void gib_moi_mehra_rengdropfa_her(int anzahlH, int anzahlR, int xRichtung){
        ZEICHENFENSTER.gibFenster().loescheAlles();
        wolke=new WOLKE(anzahlR, anzahlH, xRichtung);
    }
    

}
