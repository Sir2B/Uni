/**
 * Created by Tobias on 26.02.2015.
 */
interface Func {
    public double value (double x);
}

class TFunc1 implements Func {
    public double value( double x) {
        return( Math.cos(x) -x);
    }

}
class TFunc2 implements Func {
    public double value( double x) {
        return( Math.exp(-x) -x);
    }

}

class TFunc3 implements Func {
    public double value (double x){
        return (Math.exp(x)-Math.pow(x, 10));
    }
}
class MySin implements Func {
    public double value(double x) {
        return (Math.sin(x));
    }
}