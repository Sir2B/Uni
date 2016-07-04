
public class PILOT extends PERSONAL 
{
    protected int rang;
    public PILOT()
    {
        
    }
    
    public void befoerdern()
    {
     rang++;
     grundgehalt=grundgehalt*1.05;
     
    }
    
    public double gehaltBerechnen()
    {
        return grundgehalt+rang*150;
    }

}
//kommentar