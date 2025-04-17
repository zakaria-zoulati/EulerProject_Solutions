limit = 10_001

def isPalindrome(n): 
    s = str(n) 
    for i in range( 0 , len(s) ) :
        if( s[i] != s[ len(s) - 1 -i ] ) :
            return False 
    return True

def reverse(n): 
    rs = 0  
    while n > 0: 
        rs = rs * 10 + (n % 10) 
        n //= 10 
    return rs

rs = 0 
for i in range(1, limit):
    num = i
    found = False
    for _ in range(50):
        num = num + reverse(num)
        if isPalindrome(num):
            found = True
            break
    if not found:
        rs += 1

print(rs)
