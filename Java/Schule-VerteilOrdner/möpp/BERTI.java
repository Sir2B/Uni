import javax.swing.*;
import java.awt.event.*;

public class BERTI
{
    public JButton Button1;
    public JButton Button2;
    public JButton Button3;
    public JLabel Label;
    
    public BERTI()
    {
     Button1 = new JButton("Button 1");  
     Button2 = new JButton("Button 2");
     Button3 = new JButton("Button 3");
     Label = new JLabel("");
     
     
   Button1.addActionListener(new ActionListener()
                {public void actionPerformed(ActionEvent e)
                    {
                            Label.setText("Sie haben Button 1 gedr�ckt.");
                    }
     
                });
                
                Button2.addActionListener(new ActionListener()
                {public void actionPerformed(ActionEvent e)
                    {
                            Label.setText("Sie haben Button 2 gedr�ckt.");
                    }
     
                });
                
                Button3.addActionListener(new ActionListener()
                {public void actionPerformed(ActionEvent e)
                    {
                            Label.setText("Sie haben Button 3 gedr�ckt.");
                    }
     
                });
                
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Button1, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Button2, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Button3, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(Label, "unten");
    }
    

}
