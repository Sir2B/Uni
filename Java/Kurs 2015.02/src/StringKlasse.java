import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 * Created by Tobias on 25.02.2015.
 */
public class StringKlasse {
    public static void main(String[] args) throws IOException {
        FileReader Datei = new FileReader("Tag3/src/semester.dat");
        BufferedReader Puffer = new BufferedReader(Datei);
        String line;
        int counter = 0;
        while(true){
            line = Puffer.readLine();
            counter++;
            if (line == null){
                break;
            }
        }
//        while ((line = Puffer.readLine()) != null){
//            counter++;
//        }
        System.out.println("Anzahl Zeilen: " +counter);
    }
}
