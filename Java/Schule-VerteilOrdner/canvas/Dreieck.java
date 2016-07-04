                                                                     
                                                                     
                                                                     
                                             
import java.awt.*;

//Die Klasse DREIECK
public class Dreieck{
    
    //Attribute
    private int hoehe;
    private int laenge;
    private int xPosition;
    private int yPosition;
    private String fuellfarbe;
    private boolean istSichtbar;

    //Konstruktor
    public Dreieck(){
        hoehe = 40;
        laenge = 70;
        xPosition = 50;
        yPosition = 15;
        fuellfarbe = "green";
        istSichtbar = false;
    }
    
    //Weitere Methoden
    public void sichtbarMachen(){
        istSichtbar = true;
        zeichnen();
    }
    
 
    public void unsichtbarMachen(){
        loeschen();
        istSichtbar = false;
    }
    
    
    public void nachRechts(){
        bewegeHorizontal(20);
    }

    public void nachLinks(){
        bewegeHorizontal(-20);
    }

    public void nachOben(){
        bewegeVertikal(-20);
    }

    public void nachUnten(){
        bewegeVertikal(20);
    }


   public void bewegeHorizontal(int strecke){
        loeschen();
        xPosition = xPosition + strecke;
        zeichnen();
    }

    public void bewegeVertikal(int strecke){
        loeschen();
        yPosition = yPosition + strecke;
        zeichnen();
    }

    
    public void bewegeLangsamHorizontal(int strecke){
        int delta;

        if(strecke < 0){
            delta = -1;
            strecke = -strecke;
        }
        else{
            delta = 1;
        }

        for(int i = 0; i < strecke; i++){
            xPosition = xPosition+delta;
            zeichnen();
        }
    }


    public void bewegeLangsamVertikal(int strecke){
        int delta;

        if(strecke < 0){
            delta = -1;
            strecke = -strecke;
        }
        else{
            delta = 1;
        }

        for(int i = 0; i < strecke; i++){
            yPosition = yPosition+delta;
            zeichnen();
        }
    }


    public void groesseSetzen(int neueHoehe, int neueLaenge){
        loeschen();
        hoehe = neueHoehe;
        laenge = neueLaenge;
        zeichnen();
    }
    
    //Ändert die Farbe. Erlaubt sind "red", "yellow", "blue", "green", "magenta" und "black".
    public void fuellfarbeSetzen(String neueFarbe){
        fuellfarbe = neueFarbe;
        zeichnen();
    }


    //Zeichnet das Dreieck auf die Leinwand (Canvas)
    private void zeichnen(){
        if(istSichtbar) {
            Canvas canvas = Canvas.getCanvas();
            int[] xpoints = { xPosition, xPosition + (laenge/2), xPosition - (laenge/2) };
            int[] ypoints = { yPosition, yPosition + hoehe, yPosition + hoehe };
            canvas.draw(this, fuellfarbe, new Polygon(xpoints, ypoints, 3));
            canvas.wait(10);
        }
    }

    //Entfernt das Dreieick von der Leinwand (Canvas)
    private void loeschen(){
        if(istSichtbar) {
            Canvas canvas = Canvas.getCanvas();
            canvas.erase(this);
        }
    }
} //Ende der Klasse DREIECK

