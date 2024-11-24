import java.io.File;
import java.io.FileNotFoundException ; 
import java.util.Scanner;

public class solution { 
    public static void main( String[] args ){
        try {
            File f = new File( "in.txt" ) ; 
            Scanner sc = new Scanner(f) ; 
            int[][] g = new int[20][20] ; 
            int curr = 0 ; 
            while( sc.hasNextInt() ){
                g[curr/20][curr%20] = sc.nextInt() ; 
                curr++ ; 
            }
            int max = 0 ; 
            for(int i=0 ; i<17  ; ++i){
                for( int j=0 ; j<17 ; ++j ){
                    max = Math.max( max , g[i][j]*g[i][j+1]*g[i][j+2]*g[i][j+3] ) ; 
                    max = Math.max( max , g[i][j]*g[i+1][j]*g[i+2][j]*g[i+3][j] ) ; 
                    max = Math.max( max , g[i][j]*g[i+1][j+1]*g[i+2][j+2]*g[i+3][j+3] ) ; 
                }
            }

            for( int i=19 ; i>=3 ; --i ){
                for( int j=0 ; j<17 ; ++j ){
                    max = Math.max( max , g[i][j]*g[i-1][j+1]*g[i-2][j+2]*g[i-3][j+3] ) ; 
                }
            }

            for( int i=17 ; i<20 ; ++i ){
                for( int j=0 ; j<17 ; ++j  ){
                    max = Math.max( max , g[i][j]*g[i][j+1]*g[i][j+2]*g[i][j+3] ) ; 
                }
            }
          
            for( int j=17 ; j<20 ; ++j ){
                for( int i=0 ; i<17 ; ++i  ){
                    max = Math.max( max , g[i][j]*g[i+1][j]*g[i+2][j]*g[i+3][j] ) ; 
                }
            }

            System.out.println( max ) ; 

        } catch (FileNotFoundException e) {
            System.out.println("Zzzzz ... ") ; 
        }  

    }
}