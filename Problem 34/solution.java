public class solution {
    public static void main( String[] args ){
        // Precompute The factorial of the digits  
        int[] fact = new int[10] ; 
        fact[1] = fact[0] =  1 ;  
        for( int i=2 ; i<10 ; ++i ){
            fact[i] = fact[i-1]*i ; 
        }
        int rs = 0 ;
        // Brainstorm moment to find out the interval of The solution 
        // Really important I need This 
        // We check up to 7-didgit numbes
        // For a n-digit number , The maximum sum of factorials is n x 9! 
        // If This value is less than The small n-th digit number SO we stop at n 
        // For n+1 and higher . It's obvious , You can do some paper fast demonstartion 
        int max = (int) Math.pow( 10 , 8 ) ; 
        for( int i=10 ;  i<max ; ++i ){
            int curr = i ; 
            int sum = 0 ;
            while( curr != 0 ){
                sum += fact[curr%10]  ; 
                curr /= 10 ; 
            }
            if( sum == i ){
                rs += i ; 
            }
        }
        System.out.println(rs) ; 
    }
}