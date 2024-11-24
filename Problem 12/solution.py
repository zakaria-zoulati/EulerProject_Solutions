import math 
import time

def divs(n):
    count = 0
    a = int(math.sqrt(n))
    for i in range(1,  a+ 1):
        if n % i == 0:
            count += 2  
    if a*a == n : 
        count -= 1 
        
    return count

def main()  : 
    t = 500
    curr = 28
    add  = 8  
    while( divs( curr ) <= t  ) :
        curr += add 
        add += 1 
    print(curr) 

startTime = time.time() 
main() 
print( time.time() - startTime )
