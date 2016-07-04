import java.awt.*;

/**
 * Created by Tobias on 26.02.2015.
 */
public abstract class Shape {
    void setColor(Color red){
        System.out.println("Hi, this is method setColor from class Shape");
    }
    abstract void reDraw();
}
