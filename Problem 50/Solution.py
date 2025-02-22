limit = 25_000 

def isPrime( n ) : 
    if n == 2 or n == 3:
        return True 
    if n % 2 == 0  or n % 3 == 0  or n % 5 == 0 : 
        return False 
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


primes = [ 2 , 3 , 5] 

for i in range( 7 , limit , 2 ) :
    if isPrime( i ) :
        primes.append( i )

best = 21 
res = 953
for i in range( 0 , len(primes) ) :
    for j in range( i+21 , len(primes) , 2 ) :
        curr = 0 
        for k in range( i , j ) :
            curr += primes[k] 
        if curr > 1_000_000 :
            break 
        if isPrime( curr ) and j-i+1>=best :
            res = curr 
            best = j-i+1


print( best ) # The number of terms 
print( res )  # The Largest Prime
