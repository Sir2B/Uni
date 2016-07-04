/**
 * Created by Tobias on 25.02.2015.
 */
public class Complex {
    private double re, im;
    // constructor
    public Complex( double xr, double xi) {
        this.re = xr;
        this.im = xi;
    }
    // methods
    public Complex Mult( Complex a ) {
        double rn = this.re * a.re - this.im * a.im;
        double in = this.re * a.im + this.im * a.re;
        return( new Complex(rn, in) );
    }
    public Complex Mult(double a){
        return( new Complex(a*re, a*im));
    }
    public String toString() {  // convert to string
        String s = "( " + re + ",  i" + im + ")";
        return s;
    }
    public Complex Add(Complex other){
        return new Complex(re+other.re, im+other.im);
    }
    public Complex clone(){
        return this;
    }
    public double getRad(){
        return Math.sqrt(re*re+im*im);
    }
    public double getExp(){
        if (im>0){
            return Math.acos(re/this.getRad());
        }else{
            return -Math.acos(re/this.getRad());
        }
    }

}