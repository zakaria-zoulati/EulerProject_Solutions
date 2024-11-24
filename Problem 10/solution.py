t=2000000-1

def isPrime(n) : 
    if n == 2 or n == 3 :
        return True 
    if n % 2 == 0 : 
        return False 
    if n % 3 == 0 : 
        return False
    i = 5  
    while i*i <= n : 
        if n % i == 0 or n%(i+2) == 0 : 
            return False 
        i += 6 
    return True 
    

rs = 2
while t > 1 : 
    if isPrime(t) : 
        rs += t 
    t -= 2
# Print The final Result
print(rs)