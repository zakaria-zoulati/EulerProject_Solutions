public class solution {
    public static void main( String[] args ){
        int n = 10_000 ; 
        int sum = 0 ; 
        boolean[] isSeen = new boolean[n+1] ; 
        for( int i=1 ; i<=10_000 ; ++i ){
            if( !isSeen[i] ){
                int val = getSum( i ) ; 
                if( val != i &&  getSum(val) == i  ){
                    sum += i ; 
                    sum += val ; 
                    if( val <= n ){
                        isSeen[val] = true ; 
                    }
                }
            }
        }
        System.out.println( sum ) ; 
    }
    public static int getSum( int n ){
        int sum = 0 ; 
        for( int i=1 ; i<n ; ++i ){
            if( n%i == 0 ) sum += i ; 
        }
        return sum ; 
    }
}