public class solution {
    public static void main(String[] args) {
        int n1 = 1 ; 
        int n2 = 2 ; 
        int b = 4_000_000 ; 
        long sum = 0L ; 
        while( n2 < b ){
            if( n2 % 2 == 0 ){
                sum += n2 ; 
            }
            int temp = n2 ; 
            n2 += n1  ;
            n1 = temp ; 
        }
        System.out.println(sum) ; 
    }
}
