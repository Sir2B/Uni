import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

/**
 * Created by Tobias on 24.02.2015.
 */
public class Einlesen {
    public static void main(String[] args) throws IOException {
        System.out.println(Arrays.toString(args));
        System.out.println(System.getProperty("user.dir"));
        FileReader Datei = new FileReader("Tag2/src/numbers.dat");
        BufferedReader Puffer = new BufferedReader(Datei);
        String line;
        double[] MyArray = new double[100];
        int counter= 0;
        //System.out.println(line);
        while((line = Puffer.readLine()) != null) MyArray[counter++] = Double.parseDouble(line);
        Arrays.sort(MyArray);
        System.out.println(Arrays.toString(MyArray));
        System.out.printf("kleinster Wert: %.2f %n", MyArray[0]);
        System.out.printf("kleinster Wert: %f %n", MyArray[0]);
        System.out.println("kleinster Wert: " + MyArray[0]);
        System.out.print("kleinster Wert: " + MyArray[0] +"\n");
        System.out.printf("größter Wert: %,2f %n", MyArray[MyArray.length - 1]);

    }
}
