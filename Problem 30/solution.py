limit = 295245
arr = [ i**5 for i in range(0,10) ]

def isValid(n) :
    inter = 0 
    num = n 
    while( n > 0 ) : 
        inter += arr[ int(n%10) ]
        n /= 10
    return num == inter     

rs = 0   
for i in range( 2 , limit ):
    if isValid(i):
        rs += i 

print(rs)