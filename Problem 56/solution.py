def count( n ) : 
    rs = 0 
    while n > 0 : 
        rs += (n % 10) 
        n //= 10 
    return rs

rs  = 0 

for i in range( 1 , 100 ) : 
    for j in range( 1 , 100 ) : 
         rs = max(rs, count(pow(i, j)))


print( rs )