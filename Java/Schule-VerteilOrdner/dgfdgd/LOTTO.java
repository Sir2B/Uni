import javax.swing.*;
import java.awt.event.*;


public class LOTTO
{
    public int[] Smoky, Vier, Richtige, Insgesamt;
    public int x, zaehler, zw, a;
    private JButton schaltknopf;
    private JButton clear;
    private JButton fuenzig;
    private JLabel liste;
                                      
   public LOTTO()
    {
        Smoky = new int[6];
        Vier = new int[6];
        Richtige = new int[7];
        Insgesamt = new int[7];
        liste = new JLabel("");
        x = 0;
        
        schaltknopf = new JButton("Neues Spiel");
        clear = new JButton("Clear");
        fuenzig = new JButton("5000000.Mal");
        schaltknopf.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                einmal();
            }
            //Fabe schreibt alles ab!!
        });
        fuenzig.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                auto(5000000);
                
            }
            //Fabe schreibt alles ab!!
        });
        clear.addActionListener(new ActionListener()
        {public void actionPerformed(ActionEvent e)
            {
                for (int l=0; l<7; l++){
                    Richtige[l]=0;
                    Insgesamt[l]=0;
                }
                liste.setText("  0:" +Richtige[0] +" 1:" +Richtige[1] +" 2:" +Richtige[2] +" 3:" +Richtige[3] +" 4:" +Richtige[4] +" 5:" +Richtige[5] +" 6:" +Richtige[6]);
                
            }
            
        });
        
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(clear, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(schaltknopf, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(fuenzig, "unten");
        ZEICHENFENSTER.gibFenster().komponenteHinzufuegen(liste, "unten");
        
    }
    
   public void smoky(){
        //zufallszahlen
        zaehler=0;
        do {
            zw= (int)Math.round(Math.random()*48)+1;
            if (zw != Smoky[0] && zw != Smoky[1] && zw != Smoky[2] && zw != Smoky[3] && zw != Smoky[4] && zw != Smoky[5]){
                Smoky[zaehler]=zw;
                zaehler++;
            }}
            while (zaehler<6);
        
        //eigene Zahlen
        Vier[0]=4;
        Vier[1]=13;
        Vier[2]=19;
        Vier[3]=25;
        Vier[4]=33;
        Vier[5]=47;
        //sortieren
        int tmp=0;
        for(int a=0; a<5; a++){
            for(int i=5; i>0; i--){
                if(Smoky[i]<Smoky[i-1]){
                    tmp=Smoky[i];
                    Smoky[i]=Smoky[i-1];
                    Smoky[i-1]=tmp;
                }
            }
        }
        //vergleich
        a=0;
        for(int i=0; i<6; i++){
            for(int c=0; c<6; c++){
                if (Vier[i]==Smoky[c]){
                    a++;
                }
            }
        }
        for (int l=0; l<7; l++){
            if (a==l){Insgesamt[l]++;Richtige[l]++;}
        }
        
        
        
        //liste.setText("   "+a+" Richtige!");
        liste.setText("  0:" +Insgesamt[0] +" 1:" +Insgesamt[1] +" 2:" +Insgesamt[2] +" 3:" +Insgesamt[3] +" 4:" +Insgesamt[4] +" 5:" +Insgesamt[5] +" 6:" +Insgesamt[6]);
        
       
    }
    public void einmal(){
        smoky();
        //dauert ends lange
        for (int i=0; i<6; i++){
            System.out.println((i+1) +".Eigene Zahl:" +Vier[i] +" - Gezogene Zahlen: " +Smoky[i]);
        }
        
        System.out.println();
        System.out.println("Sie haben "+a+" Richtige!");
        System.out.println("-------------------------------------");
        System.out.println();
        
    }
    
    public void auto(int anzehl){
        
        for (int p=0; p<anzehl; p++){
            smoky();
        }
        System.out.println();
        System.out.println("Anzahl: "+anzehl);
        for (int k=0; k<7; k++){
            
            System.out.println(k +" Richtige: " +Richtige[k]);
        }
        for (int l=0; l<7; l++){
            Richtige[l]=0;
        }
    }
  
  
  
}    


