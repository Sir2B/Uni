import javax.swing.*;
import java.awt.event.*;

public class UEBUNG
{
    public JButton Button1, Button2, Button3;
    public JLabel Label;
    
    public UEBUNG()
    {
        Button1 = new JButton("Button 1");
        Button2 = new JButton("Button 2");
        Button3 = new JButton("Button 3");
        Label = new JLabel("");
        
        Button1.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {               
                Label.setText("Es wurde Button 1 gedr�ckt.");
            }
         });
        Button2.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {               
              Label.setText("Es wurde Button 2 gedr�ckt."); 
            }
         });
        Button3.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {               
            Label.setText("Es wurde Button 3 gedr�ckt."); 
            }
         });
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Button1, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Button2, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Button3, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Label, "unten");
       
    }

}
