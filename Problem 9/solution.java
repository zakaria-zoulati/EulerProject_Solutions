public class solution {
    public static void main( String[] args ){
        int a=0 , b=0 , c=0 ; 
        all:for( a = 1 ; a<1000 ; ++a ){
                for( b = a+1 ; b<1000 ; ++b ){
                    for( c = b+1 ; c<1000 ; ++c ){
                        if( a+b+c == 1000 && c*c == a*a + b*b ){
                            break all ; 
                        }
                    }
                }
        }
        System.out.println(a*b*c) ; 
    }
}