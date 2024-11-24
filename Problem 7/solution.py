from math import  sqrt

n = 10001

def isPrime(n) : 
    a = int(sqrt(n)) 
    for i in range( 2,a+1 ) : 
        if n % i == 0 : 
            return False 
    return True

curr = -1 
i = 2
while n > 0 :
    if isPrime(i) : 
        curr = i 
        n -= 1
    i += 1 

print(curr)