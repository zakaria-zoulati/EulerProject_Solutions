
public class solution {
    public static void main( String[] main ){
        int rs = 4 ; 
        int top = 1_000_000 ; 
        boolean[] isSeen = new boolean[top+1] ; 
        for( int i=11 ; i<=top ; ++i ){
            if( isPrime(i) && isValid(i) ){
                rs++ ; 
            }
        }
        System.out.println( rs ) ; 
    }
    public static boolean isValid( int n ){
        String in = String.valueOf( n ) ; 
        int len = in.length() ; 
        for( char c : in.toCharArray() ){
            if( ( c - '0' ) % 2 == 0 ){
                return false  ; 
            }
        } 
        for( int i=0 ; i<len-1 ; ++i ){
            n = ( n % 10)*( (int) Math.pow( 10 , len -1 )  )  + n/10 ;
            if( !isPrime(n) ){
                return false  ; 
            } 
        }
        return true ;
    }
    public static boolean isPrime(int n) {
        if (n <= 1) return false;
        if (n <= 3) return true;
        if (n % 2 == 0 || n % 3 == 0) return false;
        for (int i = 5; i * i <= n; i += 6) {
            if (n % i == 0 || n % (i + 2) == 0) return false;
        }
        return true;
    }
}