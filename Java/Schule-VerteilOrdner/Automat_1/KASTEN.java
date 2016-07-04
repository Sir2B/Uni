import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.awt.geom.*;

public class KASTEN
{
    private int links, oben;
    public int zahl, zahl2;
    public int var1, var2, var3;
    public int kleinergewinn, grossergewinn;
    public int AnzahlWdh;
    public int automatischAnzahl;
    private JButton schaltknopf;
    private JLabel zaehler;
    private JLabel anzeige;
    private JLabel zaehler2;
    
    public KASTEN()
    {
        zahl = 0;
        links = 50;
        oben = 100;
        AnzahlWdh = 2000;
        kleinergewinn = 2;
        grossergewinn = 30;
        schaltknopf = new JButton("Neues Spiel");
        zaehler = new JLabel("");
        anzeige = new JLabel("");
        zaehler2 = new JLabel("");
                
        schaltknopf.addActionListener(new ActionListener()
        { public void actionPerformed(ActionEvent e) {
                fuelle();}});
                
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen (schaltknopf, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen (zaehler2, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen (anzeige, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen (zaehler, "unten");
                
        zeichne();
    }
    
      
  
     public int zufaelligeZahl(int n) {
        
        // Zufallszahl zwischen 0.1 & 1.0 erzeugen
        double dezimalZahl = Math.random();

        // Wert in den Bereich 0 bis n strecken
        int ganzZahl = (int)Math.round( dezimalZahl * n );

        // Ergebnis zurueckgeben
        return ganzZahl;     
        
    } 
    public void zeichnesmilie()
    {
        ZEICHENFENSTER.gibFenster().fuelleKreis(links,oben,40,"gruen");
        ZEICHENFENSTER.gibFenster().fuelleKreis(links,oben,30,"weiss");
        ZEICHENFENSTER.gibFenster().fuelleKreis(links-10,oben-5,10,"rot");
        ZEICHENFENSTER.gibFenster().fuelleKreis(links+10,oben-5,10,"rot");
        ZEICHENFENSTER.gibFenster().fuelleRechteck(links-10,oben+10,20,5,"rot");
}
     public void zeichne()
    {
        ZEICHENFENSTER.gibFenster().zeichneRechteck(links-50,oben-55,120,120);
        ZEICHENFENSTER.gibFenster().zeichneRechteck(links+70,oben-55,120,120);
        ZEICHENFENSTER.gibFenster().zeichneRechteck(links+190,oben-55,120,120);
        ZEICHENFENSTER.gibFenster().zeichneKreis(links+10,oben,50);
        ZEICHENFENSTER.gibFenster().zeichneKreis(links+130,oben,50);
        ZEICHENFENSTER.gibFenster().zeichneKreis(links+250,oben,50);
        
}
    public void fuelle()
    {

        ZEICHENFENSTER.gibFenster().loescheKreis(links+250,oben+300,80);
        var1 = zufaelligeZahl(8);
        var2 = zufaelligeZahl(8);
        var3 = zufaelligeZahl(8);
        ZEICHENFENSTER.gibFenster().fuelleKreis(links+10,oben,50,var1);
        ZEICHENFENSTER.gibFenster().fuelleKreis(links+130,oben,50,var2);
        ZEICHENFENSTER.gibFenster().fuelleKreis(links+250,oben,50,var3);
        zahl++;
        zaehler.setText(""+zahl+"  ");
        zahl2=zahl2-1;
        
        //Gewinnausschüttung
        if(var1 == var3 && var2 == var3){
                anzeige.setText("Hauptgewinn! "+grossergewinn +"€");
                zahl2 = zahl2 + grossergewinn;
               
            }
        else if(var1 == var2){
            
             anzeige.setText("kleiner Gewinn! "+kleinergewinn +"€ ");
             zahl2 = zahl2 + kleinergewinn;
        }
        else if(var2 == var3){
                anzeige.setText("kleiner Gewinn! "+kleinergewinn +"€ ");
                zahl2 = zahl2 + kleinergewinn;
        }
        else if(var1 == var3){
                anzeige.setText("kleiner Gewinn! "+kleinergewinn +"€");
                zahl2 = zahl2 + kleinergewinn;
        }
     
        else {
            anzeige.setText("leider nix! -7€ ");
        }
        
        zaehler2.setText(" Geld:  "+zahl2+"€  ");
        
            
}

        public void blinke()
        {
             
            for(int i = 0; i < AnzahlWdh; i++){
                
            ZEICHENFENSTER.gibFenster().fuelleKreis(links+250,oben,50,zufaelligeZahl(8));
            ZEICHENFENSTER.gibFenster().warte(10);
        }
            
    }
        public void automatisch (int automatischAnzahl)
        {
            
            for(int e = 0; e < automatischAnzahl; e++) {
                fuelle();
                ZEICHENFENSTER.gibFenster().warte(0);
            }
            
        
      }


    
}