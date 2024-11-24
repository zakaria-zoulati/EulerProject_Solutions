public class solution {

    public static boolean isPalindrom( int n ){
        int org = n ;
        int rev = 0 ; 
        while( n > 0){
            rev = rev*10 + n%10 ; 
            n /= 10 ; 
        }
        return rev == org ; 
    }


    public static void main( String[] args ){
        int max = -1  ;
        for( int i=100 ; i<=999 ; ++i ){
            for( int j=i ; j<=999 ; ++j ){
                if( isPalindrom(i*j) ){
                    max = Math.max( i*j , max ) ;
                }
            }
        }
        System.out.println(max) ; 
    }
}