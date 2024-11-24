public class solution2 {
    public static void main( String[] args ){
        int s = 1000 ; 
        for( int a = 1 ; a<s ; ++a ){
                for(int b = a+1 ; b<s-a; ++b ){
                    int c = s - a - b ; 
                    if( a*a + b*b == c*c ){
                        System.out.println(a*b*c) ; 
                    }
                }
        }
    }
}