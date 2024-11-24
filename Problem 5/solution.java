public class solution {
    public static void main(String[] args) {
        long rs = 1L ; 
        boolean[] isSeen = new boolean[21] ; 
        for( int i=2 ; i<=20 ; ++i ){
            if( isSeen[i] ) continue ; 
            isSeen[i] = true ; 
            int curr = i ; 
            while( curr *i <=20 ){
                curr *= i ; 
            }
            for( int j=2*i ; j<=20 ; j += i ){
                isSeen[j] = true ; 
            }
            rs *= curr ; 
        }
        System.out.println(rs) ; 
    }
}
