import math 
import time

def divs(n):
    count = 0
    a = int(math.sqrt(n))
    for i in range(1,  a+ 1):
        if n % i == 0:
            count += 2  # Count both i and n/i
    if a*a == n : 
        count -= 1 
        
    return count


t = 500
curr = 28
add  = 8  
while( divs( curr ) <= t  ) :
    curr += add 
    add += 1 

print( curr )
