mod = 10_000_000_000

sum = 0 

def mex( a , b ) :
    if( b == 0 ) :
        return 1
    if( b == 1 ) :
        return a
    curr = a
    a = a * a % mod 
    if b % 2 == 0 : 
        return mex( a , b//2 ) % mod
    else :
        return (mex( a , b//2 ) * curr ) % mod
        

limit = 1001
for i in range( 1 , limit ) : 
    sum = ( sum + mex(i,i) ) % mod

print(sum) 