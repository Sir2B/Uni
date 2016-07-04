
public class TASCHENRECHNER
{
    public PLUS objplus;
    public MINUS objminus;
    public GETEILT objgeteilt;
    public MAL objmal;
    public FAKULTAET objfakul;
    public POTENZIEREN objpoten;
    public WURZEL objwurzel;
    public yWURZEL objywurzel;
    public GAUSSSCHESUMMEN objgausch;
    public LOGARITHMUS objlog;
    public SINUS objsin;
    public COSINUS objcos;
    public TANGENS objtan;
    public double ergebnis;
    
    public TASCHENRECHNER()
    {
        objplus = new PLUS();
        objminus = new MINUS();
        objgeteilt = new GETEILT();
        objmal=new MAL();
        objfakul=new FAKULTAET();
        objpoten=new POTENZIEREN();
        objwurzel=new WURZEL();
        objywurzel=new yWURZEL();
        objgausch=new GAUSSSCHESUMMEN();
        objlog=new LOGARITHMUS();
        objsin=new SINUS();
        objcos=new COSINUS();
        objtan=new TANGENS();
        ergebnis = 0;
        
    }

    public double rechn(double x, double y, char z) {
    switch(z)
      {
      case '+':ergebnis = objplus.plus(x,y);break;
      case '-':ergebnis = objplus.plus(x,y);break;
      case '/':ergebnis = objgeteilt.geteilt(x,y);break;
      case '*':ergebnis =objmal.mal(x,y);break;
      case '!':ergebnis=(double)objfakul.fakultaet((int)x);break;
      case '^':ergebnis=objpoten.potenzieren(x,y);break;
      case 'w':ergebnis=objwurzel.wurzel(x);break;
      
    }
    
    return ergebnis;
    }
    
    public double rechnen(double x,double y, String z)  {
        if (z=="+") {
            ergebnis = objplus.plus(x,y);
        }
        if (z=="-") {
            ergebnis = objminus.minus(x,y); 
        }
        if(z=="/") {
            ergebnis = objgeteilt.geteilt(x,y);
        }
        if (z=="*") {
            ergebnis =objmal.mal(x,y);
        }
        if (z=="!") {
            ergebnis=(double)objfakul.fakultaet((int)x);
        }
        if (z=="^") {
            ergebnis=objpoten.potenzieren(x,y); 
        }
        if (z=="wurzel") {
            ergebnis=objwurzel.wurzel(x); 
        }
        if (z=="ywurzel") {
            ergebnis=objywurzel.ywurzel(y,x); 
        }
        if (z=="gausch") {
            ergebnis=objgausch.derkleinegauss(x,y); 
        }
        if (z=="log") {
            ergebnis=objlog.log((int)x,(int)y); 
        }
        if (z=="sin") {
            ergebnis=objsin.sin(x); 
        }
        if (z=="cos") {
            ergebnis=objcos.cos(x); 
        }
        if (z=="tan") {
            ergebnis=objtan.tan(x); 
        }
            return ergebnis;
        
    
    }
}
