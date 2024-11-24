import java.io.File;
import java.io.FileNotFoundException;
import java.util.* ; 

public class solution {
    public static void main(String[] args) {
        try {
            File file = new File("1000-number.txt") ; 
            Scanner sc = new Scanner( file ) ; 
            StringBuilder str = new StringBuilder() ; 
            while( sc.hasNextLine() ){
                str.append( sc.nextLine() ) ; 
            }
            String line = str.toString() ; 
            PriorityQueue<Long> pq = new PriorityQueue<>(
                (x,y) -> Long.compare(y , x)
            ); 
            for( int i=0 ; i+13<1000 ; ++i ){
                long p = 1L ; 
                for( int j=i ; j<i+13 ; ++j ){
                    p *= (  line.charAt(j) - '0' ) ; 
                }
                pq.add(p) ; 
            }
            System.out.println( pq.peek() ) ; 

        } catch (FileNotFoundException e) {
            System.out.println("There is an error Here")  ; 
        }
        

    }
}

