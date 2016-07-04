import java.awt.*;

public class TestShape {
    public static void main(String[] args) {
        Shape[] sarr = new Shape[3];
        sarr[0] = new Oval();
        sarr[1] = new RoundRect();
        sarr[2] = new Rectangle();
//        . . .;
        for (int i = 0; i < sarr.length; i++) {
            sarr[i].setColor(Color.red);
            sarr[i].reDraw();
//            ...;
        }
    }
}