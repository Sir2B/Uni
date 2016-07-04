import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.DoubleSummaryStatistics;
import java.util.Locale;

/**
 * Created by Tobias on 25.02.2015.
 */
public class TestStatCalc {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.ENGLISH);
        AufgabeAB();
        AufgabeC();
    }
    public static void AufgabeAB(){
        StatCalc stat = new StatCalc();
        for (int i = 0; i < 100; i++){
            stat.enter(Math.random());
        }
        System.out.println("Mittelwert: " +stat.getMean());
        System.out.println("Std.abweichung: " +stat.getStandardDeviation());
        System.out.println("Minimum: " +stat.getMin());
        System.out.println("Maxmium: " +stat.getMax());
    }
    public static void AufgabeC() throws IOException {
        FileReader Datei = new FileReader("Tag3/src/semester.dat");
        BufferedReader Puffer = new BufferedReader(Datei);
        StatCalc LMU = new StatCalc();
        StatCalc TUM = new StatCalc();
        int line_counter = 0;
        for(;;){
            System.out.println("asdhasldhk jasd");
            break;
        }
        for (;line_counter < 100; line_counter++){
            double Note = Double.parseDouble(Puffer.readLine());
            LMU.enter(Note);
        }
        for (;line_counter < 200; line_counter++){
            double Note = Double.parseDouble(Puffer.readLine());
            TUM.enter(Note);
        }
        System.out.printf("%nTUM:%n");
        System.out.printf("         Anzahl: %d%n", TUM.getCount());
        System.out.printf("     Mittelwert: %.2f%n", TUM.getMean());
        System.out.printf(" Std.Abweichung: %.2f%n", TUM.getStandardDeviation());
        System.out.printf("LMU:%n");
        System.out.printf("         Anzahl: %d%n", LMU.getCount());
        System.out.printf("     Mittelwert: %.2f%n", LMU.getMean());
        System.out.printf(" Std.Abweichung: %.2f%n", LMU.getStandardDeviation());

    }
}
