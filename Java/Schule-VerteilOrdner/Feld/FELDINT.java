
public class FELDINT
{
    public int[] zufall;


    public FELDINT()
    {
        zufall = new int[50];
        
        for (int i=0; i<49; i++) {
        zufall[i]=(int)Math.round(Math.random()*10);
       
        }
        
    }

    
    public void zufall(int y)
    {
       
       
    }
}
