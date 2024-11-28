def fact(n) :
    if n == 1 : 
        return 1 
    return n*fact(n-1)

a = fact(100) 
rs = 0 
while( a != 0 ) : 
    rs += a%10 
    a //=10 

print(rs) 