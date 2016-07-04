import java.io.*;
import java.nio.file.Files;

/**
 * Created by Tobias on 27.02.2015.
 */
public class FileCopy {
    public static void main(String[] args) throws IOException {
        if (args.length != 2){
            throw new IllegalArgumentException("\nUsage: java FileCopy file1.txt file2.txt");
        }
        File source = new File(args[0]);
        File destination = new File(args[1]);
        Files.copy(source.toPath(), destination.toPath());
    }
}
