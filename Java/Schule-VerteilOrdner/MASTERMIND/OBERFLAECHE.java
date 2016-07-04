import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class OBERFLAECHE
{
    private Color[] Lsg, Eing;
    private JButton B1, B2, B3, B4, B5, B6, B7, B8, Neu;
    private JLabel Text;
    private int zaehler, zeile;
    AUSWERTUNG mausw;
    
    public OBERFLAECHE()
    {
       Lsg = new Color[4];
        mausw = new AUSWERTUNG();
       mausw.zufallsbefuellung();
       Lsg[0] = mausw.lsg[0];
       Lsg[1] = mausw.lsg[1];
       Lsg[2] = mausw.lsg[2];
       Lsg[3] = mausw.lsg[3];
       Text = new JLabel("  Bitte Farbe auswählen! (9 Versuche)");
       Eing = new Color[4];
       zaehler=0;
       zeile=0;
      
       
       B1 = new JButton("schwarz");
       B2 = new JButton("rot");
       B3 = new JButton("grün");
       B4 = new JButton("blau");
       B5 = new JButton("gelb");
       B6 = new JButton("magenta");
       B7 = new JButton("cyan");
       B8 = new JButton("grau");
       Neu = new JButton("Neues Spiel");
       
      
       B1.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.black);
            }
        });
        
        B2.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.red);
            }
        });
        B3.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.green);
            }
        });
        B4.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.blue);
            }
        });
        B5.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.yellow);
            }
        });
        B6.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.magenta);
            }
        });
        B7.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.cyan);
            }
        });
        B8.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                befuelle(Color.gray);
            }
        });
        Neu.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
               ZEICHENFENSTER.gibFenster().loescheAlles();
               zeile=0;
               zaehler=0;
               mausw.zufallsbefuellung();
               Lsg[0] = mausw.lsg[0];
               Lsg[1] = mausw.lsg[1];
               Lsg[2] = mausw.lsg[2];
               Lsg[3] = mausw.lsg[3];  
               Text.setText("Neues Spiel!  Sie haben noch 9 Versuche!");
               
            }
        });
       
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Neu, "unten");
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B1, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B2, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B3, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B4, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B5, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B6, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B7, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(B8, "unten"); 
       ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Text, "unten");
       
       
       ZEICHENFENSTER.gibFenster().zeichneKreis(100,50,30);
       ZEICHENFENSTER.gibFenster().zeichneKreis(200,50,30);
       ZEICHENFENSTER.gibFenster().zeichneKreis(300,50,30);
       ZEICHENFENSTER.gibFenster().zeichneKreis(400,50,30);
       
       
       //ZEICHENFENSTER.gibFenster().setzeVordergrundFarbe(colorZuFarbe(Color.green));
       //ZEICHENFENSTER.gibFenster().zeichneText("IDIOT",50,50);
    }
    
    private String colorZuFarbe(Color color)
    {
        if (color==Color.white) return "weiss";
        if (color==Color.black) return "schwarz";
        if (color==Color.red) return "rot";
        if (color==Color.green) return "gruen";
        if (color==Color.blue) return "blau";
        if (color==Color.yellow) return "gelb";
        if (color==Color.magenta) return "magenta";
        if (color==Color.cyan) return "cyan";
        if (color==Color.gray) return "grau";
        return "";
    }
    
    public void befuelle(Color farbe){
        
        ZEICHENFENSTER.gibFenster().fuelleKreis(100+100*zaehler,50+70*zeile,30,colorZuFarbe(farbe));
        Eing[zaehler]=farbe;
        zaehler++;
        if (zaehler==4) {
            zaehler=0;
            mausw.Inpeing(Eing);
            mausw.InpLsg(Lsg);
            mausw.auswerten();
            markenmalen(mausw.nblack,mausw.nwhite);
            
            zeile++;
            
        }
    }
    
     
    
    public void markenmalen(int schwarz, int weiss){
        int zz = 0;
        for (int i=0; i<schwarz; i++){
            ZEICHENFENSTER.gibFenster().fuelleKreis(490+zz*30,50+70*zeile,10,"schwarz");
            zz++;
        }
        for (int i=0; i<weiss; i++){
            ZEICHENFENSTER.gibFenster().zeichneKreis(490+zz*30,50+70*zeile,10);
            zz++;
        }
        Text.setText("  Noch " +(8-zeile) +" Versuche!");
        
        if (schwarz == 4) {
            Text.setText("  Sie haben gewonnen mit " +(zeile+1) +" Versuchen!");
            
        }
        if (zeile == 8 && schwarz != 4) 
            {
            Text.setText("  IDIOTA");
            loesungmalen();
            
            
            }
    
    }
    public void loesungmalen(){
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,50,30,colorZuFarbe(mausw.lsg[0]));
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,150,30,colorZuFarbe(mausw.lsg[1]));
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,250,30,colorZuFarbe(mausw.lsg[2]));
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,350,30,colorZuFarbe(mausw.lsg[3]));
    }
    public void loesungloeschen(){
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,50,30,"weiss");
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,150,30,"weiss");
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,250,30,"weiss");
        ZEICHENFENSTER.gibFenster().fuelleKreis(700,350,30,"weiss");
    }

    
}
