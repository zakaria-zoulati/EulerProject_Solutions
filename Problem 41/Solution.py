def isPrime(n):
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6  
    return True 

def isValid(n):
    if n%3 == 0 or n%5 == 0 :
        return False  
    sum = 0 
    count = 0
    s = set()  
    while n > 0:
        digit = n % 10
        if digit==0 or digit in s : 
            return False 
        s.add(digit)
        sum += digit 
        count += 1
        n //= 10
    return sum == count*(count+1)//2
    

largest = 9_999_999

while True :    
    if  isValid(largest) and isPrime(largest)  : 
        print( largest ) 
        break  
    largest -= 2  