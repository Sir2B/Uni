public class LOTTO
{
    // instance variables - replace the example below with your own
    public int[] Smoky, Vier, Richtige;
    public int x, zaehler, zw;
                                      
   public LOTTO()
    {
        Smoky = new int[6];
        Vier = new int[6];
        Richtige = new int[7];
        x = 0;
        
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
        int a=0;
        for(int i=0; i<6; i++){
            for(int c=0; c<6; c++){
                if (Vier[i]==Smoky[c]){
                    a++;
                }
            }
        }
        for (int l=0; l<7; l++){
            if (a==l){Richtige[l]++;}
        }
        
        //dauert zu lange
        //System.out.println();
        //System.out.println("Sie haben "+a+" Richtige!");
       
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


