import java.io.*;
import java.util.concurrent.TimeUnit;
import java.math.*;

public class file_transfer {
    public static void main(String[] args) {
        long start = System.nanoTime();
        String name = new String(args[0]);
        File file_in = new File(name);
        File file_out = new File("Java.txt");
        try {
            BufferedReader br = new BufferedReader(new FileReader(file_in));
            BufferedWriter bw = new BufferedWriter(new FileWriter(file_out));
            String line = null;
            while((line = br.readLine()) != null) {
                bw.write(line);
            }
        }
        catch(Exception ex) {
            ex.printStackTrace();
        }
        long end = System.nanoTime();
        double time = (double)(end-start);
        time = time/Math.pow(10,9);
        System.out.println(time);
    }
}
