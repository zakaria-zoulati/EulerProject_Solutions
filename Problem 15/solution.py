def fact(n): 
    if( n == 1 ) :
        return 1 
    return n*fact(n-1) 

a = fact(40) 
b = fact(20) 

rs = a//(b*b)
print(rs) 