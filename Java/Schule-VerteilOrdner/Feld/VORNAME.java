

public class VORNAME
{
    public String[] name;
    
    
    public VORNAME()
    {
        
        name = new String[25];
        
        namen();
       
    }

   public void namen() {
    name[0]="Anna";
    name[1]="Axel";
    name[2]="Benedikt";
    name[3]="Christoph";
    name[4]="Fabian";
    name[5]="Florian";
    name[6]="Florian";
    name[7]="Franz";
    name[8]="Franzi";
    name[9]="Johannes";
    name[10]="Johannes";
    name[11]="Johannes";
    name[12]="Johannes";
    name[13]="Josef";
    name[14]="Manuel";
    name[15]="Matthias";
    name[16]="Maxi I";
    name[17]="Maxi II";
    name[18]="Miriam";
    name[19]="Nicol";
    name[20]="Niklas";
    name[21]="Richard";
    name[22]="Sebastian";
    name[23]="Tobias";
    name[24]="Vitus";
    
    
    }
    public void ausgeben(){
    
        for (int xy=0; xy<25; xy++) {
            
            System.out.println(name[xy]); 
            
        }
        
    }
    
    public void umsortieren(){
        
        String xy;
        for (int i=0; i<12; i++) 
        {
            xy = name[i];
            name[i] = name[24-i];
            name[24-i] = xy;
            
            
        }
       ausgeben(); 
    }    
}
