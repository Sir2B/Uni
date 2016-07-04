                             
import java.awt.*;
import java.awt.geom.*;
import java.awt.event.*;

//Die Klasse KREIS
public class Kreis extends KeyAdapter{

    //Attribute
    private int radius;
    private int xPosition;
    private int yPosition;
    private String fuellfarbe;
    private boolean istSichtbar;
    
    
    
   
    //Konstruktor
    public Kreis(){
        radius = 30;
        xPosition = 40;
        yPosition = 60;
        fuellfarbe = "red";
        istSichtbar = true;
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
    public void bewegeImViereck(int x, int y, int anzahl){
        int delta;
        
        for(int i = 0; i < anzahl; i++) {
            
        delta = 1;
        
        for(int j = 0; j < x; j++) {
            xPosition = xPosition+delta;
            zeichnen();
        }
        
        for(int j = 0; j < y; j++) {
            yPosition = yPosition+delta;
            zeichnen();
        }
        
        delta = -1;
        
        for(int j = 0; j < x; j++) {
            xPosition = xPosition+delta;
            zeichnen();
        }
        
        for(int j = 0; j < y; j++) {
            yPosition = yPosition+delta;
            zeichnen();
        }
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


    public void groesseSetzen(int neuerRadius){
        loeschen();
        radius = neuerRadius;
        zeichnen();
    }

    //Ändert die Farbe. Erlaubt sind "red", "yellow", "blue", "green", "magenta" und "black".
    public void fuellfarbeSetzen(String neueFarbe){
        fuellfarbe = neueFarbe;
        zeichnen();
    }

    //Zeichnet den Kreis auf die Leinwand (Canvas)
    private void zeichnen(){
        if(istSichtbar) {
            Canvas canvas = Canvas.getCanvas();
            canvas.draw(this, fuellfarbe, new Ellipse2D.Double(xPosition, yPosition, 
                                                          radius*2, radius*2));
            canvas.wait(10);
        }
    }

    //Entfernt den Kreis von der Leinwand (Canvas)
    private void loeschen(){
        if(istSichtbar) {
            Canvas canvas = Canvas.getCanvas();
            canvas.erase(this);
        }
    }
   
    //neue Methode für langsame diagonale Bewegung (Weite über den x-Wert)
   public void bewegeLangsamDiagonal(int xwert, int ywert){
       int deltaX;
       int deltaY;
       
       if (xwert < 0){
           deltaX=-1;
           xwert=-xwert;
        }
       else {
           deltaX=1;
        }
       if (ywert < 0){
           deltaY=-1;
        }
        else {
            deltaY=1;
        }
        
        for(int i=0;i<xwert;i++){
            xPosition=xPosition+deltaX;
            yPosition=yPosition+deltaY;
            zeichnen();
        }
    }
    
    //Methode zum schrägen Verschieben (x- und y-Wert werden ausgewertet)
    public void bewegeSchraeg(int x, int y){
        int betragx;
        int betragy;
        if (x<0) {
            betragx=-x;
        }
        else {
            betragx=x;
        }
        
        if (y<0) {
            betragy=-y;
        }
        else {
            betragy=y;
        }
 // Beginn erster Fall       
        if (x > 0){
  //  erster Teil y>0
            if (y >0){
            //erster Unterteil
            if (x < y) {
                bewegeLangsamDiagonal(x,y);
                bewegeLangsamVertikal(y-x);
            }
            //zweiter Unterteil
            else {
                bewegeLangsamDiagonal(y,x);
                bewegeLangsamHorizontal(x-y);
            }
        }
 //Ende erster Teil Beginn zweiter Teil (y <0)
        else {
            if (x < betragy){
                bewegeLangsamDiagonal(x,y);
                bewegeLangsamVertikal(x+y);
            }
            else {
                bewegeLangsamDiagonal(betragy,y);
                bewegeLangsamHorizontal(x+y);
            }
        }
        //Ende zweiter Teil
    }
    //ELSE Teil für x < 0 Beginn y > 0
    else { 
        if (y > 0 ) {
            if (betragx < betragy) {
                bewegeLangsamDiagonal(x,y);
                bewegeLangsamVertikal(x+y);
            }
            else {
                bewegeLangsamDiagonal(-y,y);
                bewegeLangsamHorizontal(x+y);
            }
    //und y < 0
        }
        else {
            if (betragx < betragy) {
                bewegeLangsamDiagonal(x,y);
                bewegeLangsamVertikal(y-x);
            }
            else {
                bewegeLangsamDiagonal(y,x);
                bewegeLangsamHorizontal(x-y);
            }
        }
    }
}


public void bewegeKomplettSchraeg(int x, int y) {
int betragx;
int betragy;
int h1;
int h2; 

if (x>0) {
betragx=x;
h1=1;
}
else{
betragx=-x;
h1=-1;
}
if (y>0) {
betragy=y;
h2=1;
}
else{
betragy=-y;
h2=-1;
}

if (x>y) {
for (int i=0;i<y;i++) {
                bewegeVertikal(1);
                bewegeLangsamHorizontal(Math.round(x/y));
            }
        }
else {
for (int i=0;i<x;i++) {
                bewegeHorizontal(1);
                bewegeLangsamVertikal(Math.round(y/x));
            }
        }
        
if (x>betragy) {
for (int i=0;i<betragy;i++) {
                bewegeVertikal(h2);
                bewegeLangsamHorizontal(Math.round(x/betragy));
            }
        }
                
else {
for (int i=0;i<betragx;i++) {
                bewegeHorizontal(h1);
                bewegeLangsamVertikal(Math.round(y/betragx));
            }
        }
    }//Ende von bewegekomplettschraeg
    
    public void keyPressed(KeyEvent _ke) {

    if(_ke.getKeyCode() == _ke.VK_UP){
      //Hier den Code wenn die Pfeiltaste nach oben gedrückt wurde	
      bewegeLangsamVertikal(-5);
    }
    else if(_ke.getKeyCode() == _ke.VK_DOWN){
      //Hier den Code wenn die Pfeiltaste nach unten gedrückt wurde	
      bewegeLangsamVertikal(5);
    }
    else if(_ke.getKeyCode() == _ke.VK_LEFT){
      //Hier den Code wenn die Pfeiltaste nach links gedrückt wurde	
      bewegeLangsamHorizontal(-5);
    }
    else if(_ke.getKeyCode() == _ke.VK_RIGHT){
      //Hier den Code wenn die Pfeiltaste nach rechts gedrückt wurde	
      bewegeLangsamHorizontal(5);
    }
  }
} //Ende der Klasse KREIS
