
public class NEINNNNNNNNNNNNN
{
    public int[] own;
    public int[] y;
    public int richtige0;
    public int richtige1;
    public int richtige2;
    public int richtige3;
    public int richtige4;
    public int richtige5;
    public int richtige6;
    
    public NEINNNNNNNNNNNNN()
    {
        own= new int[6];
        y= new int[6];
        
        zahlen();
        
    }

    public void zufallszahlen() {
        int zw=0;
        int zehler=0;
        do{
            zw=(int)Math.round(Math.random()*48+1);
            //if (zw != y[0] && zw =! y[1] && zw =! y[2] && zw =! y[3] && zw =! y[4] && zw =! y[5]){
            //    y[zehler]=zw;
            //    zehler++;
            //}
           }
        while (zehler <6);
            
        
        
    }
    public void zahlen(){
        own[0]=16;
        own[1]=23;
        own[2]=33;
        own[3]=5;
        own[4]=47;
        own[5]=13;
    }
    public void eigzahlen(int a0,int a1,int a2,int a3,int a4,int a5){
        own[0]=a0;
        own[1]=a1;
        own[2]=a2;
        own[3]=a3;
        own[4]=a4;
        own[5]=a5;
        
    }
    
    public void sortieren(){
        int tmp=0;
        for(int a=0; a<5; a++){
            for(int i=5; i>0; i--){
                if(y[i]<y[i-1]){
                    tmp=y[i];
                    y[i]=y[i-1];
                    y[i-1]=tmp;
                }
            }
        }
        
    }
    
    public void eigsortieren(){
        int tmp=0;
        for(int a=0; a<5; a++){
            for(int i=5; i>0; i--){
                if(own[i]<own[i-1]){
                    tmp=own[i];
                    own[i]=own[i-1];
                    own[i-1]=tmp;
                }
            }
        }
        
    }
    
    public void vergleich(){
        int a=0;
        
        for(int i=0; i<6; i++){
            for(int c=0; c<6; c++){
                if (own[i]==y[c]){
                    a++;
                }
            }
        }
        
        System.out.println("Sie haben "+a+" Richtige!");
        System.out.println();
    }
    
    
    public void ausgeben(){
        for (int xy=0; xy<6; xy++) { 
            System.out.println("Zahl "+(xy+1) +": "+y[xy]+" Eigene Zahl:"+own[xy]);  
        }
    }
    
    public void lotto(){
        zufallszahlen();
        sortieren();
        eigsortieren();
        ausgeben();
        vergleich();
    }
    
    public void lottos(int anzahl){
    for (int p=0; p<anzahl; p++){
        lotto();
    }
    }
    
    public void auto(){
       int zehler=0;
    do 
    {
        lotto();
        zehler++;
        
        
        
    }while (2<6);
}
    
}
