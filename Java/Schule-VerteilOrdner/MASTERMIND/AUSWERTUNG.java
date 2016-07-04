import javax.swing.*;
import java.awt.event.*;
import java.awt.*;

public class AUSWERTUNG
{
    
    public Color[] lsg;    
    private Color[] eing;
    public int nblack, nwhite;
    
    
    public AUSWERTUNG()
    {
        lsg = new Color[4];
        eing = new Color [4];
        /*lsg[0] = Color.green;
        lsg[1] = Color.red;
        lsg[2] = Color.yellow;
        lsg[3] = Color.blue;
        
        (eing[0] = Color.yellow;
        eing[1] = Color.black;
        eing[2] = Color.magenta;
        eing[3] = Color.blue;*/
               
        nblack = nwhite = 0;
    }

    public void InpLsg(Color ilsg[])
    {
        for(int i = 0;i<4;i++)
        {
            lsg[i] = ilsg[i];
        }
    }
    
    public void Inpeing(Color ieing[])
    {
        for(int i = 0;i<4;i++)
        {
            eing[i] = ieing[i];
        }
    }
    
    public void zufallsbefuellung()
    {
        int cfarbe;
        for(int cnt = 0;cnt<4;cnt++)
        {
            cfarbe = (int)Math.round(Math.random()*7);
            switch (cfarbe)
            {
                case 0:  lsg[cnt] = Color.black; break;
                case 1:  lsg[cnt] = Color.blue; break;
                case 2:  lsg[cnt] = Color.green; break;
                case 3:  lsg[cnt] = Color.cyan; break;
                case 4:  lsg[cnt] = Color.red; break;
                case 5:  lsg[cnt] = Color.magenta; break;
                case 6:  lsg[cnt] = Color.yellow; break;
                case 7:  lsg[cnt] = Color.gray;
            }
            if(cnt!=0)
            {
                for(int retcnt = cnt-1;retcnt>=0;retcnt--)
                {
                    if(lsg[cnt] == lsg[retcnt])
                    {
                        cnt--; 
                        retcnt = -1;
                    }
                }
            }
        }
    }
        
    public void auswerten()
    {
        nblack = nwhite = 0;
        for(int i = 0;i<4;i++)
        {
            if(lsg[i] == eing[i])
            {
                nblack++;   
            }
        }
        for(int i = 0;i<4;i++)
        {
            for(int j = 0;j<4;j++)
            {
                if(lsg[i] == eing[j])
                {
                    nwhite++;   
                }
            }
        }
        nwhite -= nblack;
        
    }
}