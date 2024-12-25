public class solution {
     public static void main( String[] args ){
        // Calculate The number of mondays between  (1 Jan 1901 to 31 Dec 2000) 
        // 1 Jan 1901 was a Monday 
        int rs = 0 ; 
        int curr = 365 ; 
        for( int i= 1901 ; i<=2000 ; ++i ){
            for( int j=1 ; j<=12 ; ++j ){
                if( curr % 7 == 6 ) ++rs ; 
                if( j == 4 || j == 6 || j == 9 || j == 11 ) curr += 30 ; 
                else if( j==2  ){
                    if( i%400 == 0 || ( i%4==0 && i%100 != 0 ) ){
                        curr += 29 ; 
                    }else {
                        curr += 28 ; 
                    }
                }else{
                    curr += 31 ; 
                }
            }
        }
        System.out.println(rs) ; 
     }
}