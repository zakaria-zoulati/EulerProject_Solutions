import java.util.* ; 
import java.io.File ; 
import java.io.FileNotFoundException ; 
import java.math.BigInteger;
public class solution {
    public static void main( String[] args ){
        try {
            File f = new File("in.txt") ;
            Scanner sc = new Scanner(f) ;  
            BigInteger bg = new BigInteger("0") ; 
            while( sc.hasNextLine() ){
                bg = bg.add( new BigInteger(sc.nextLine() )) ; 
            }
            System.out.println( bg.toString() ) ; 
        }catch (FileNotFoundException e) {
            System.out.println("Zzzzz ..") ; 
        }
    }
}