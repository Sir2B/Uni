

public class BODENPERSONAL extends PERSONAL 
{
    public double ueberstunden;
    public BODENPERSONAL()
    {
       
    }

    public void befoerdern()
    {
        grundgehalt=grundgehalt*1.02;
    }
    
    public double gehaltBerechener()
    {
        return grundgehalt+ueberstunden*25;
    }
}
