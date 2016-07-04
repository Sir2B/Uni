import javax.swing.*;
import java.awt.event.*;

public class LABEL
{
    
    private JLabel Label0;

    public LABEL()
    {
        Label0 = new JLabel("SERS");
        
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Label0, "unten");
        
    }
    
    public void LabelTextAendern(String text){
        Label0.setText(text);
    }

    
}
