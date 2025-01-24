import math

def fibonacci_digits(k):
    phi = (1 + math.sqrt(5)) / 2
    return math.floor(k * math.log10(phi) - math.log10(math.sqrt(5))) + 1

def find_first_fibonacci_with_k_digits(k):
    left, right = 1, 10000  
    while left < right:
        mid = left + (right - left) // 2
        if fibonacci_digits(mid+1) < k:  
            left = mid + 1
        else:  
            right = mid
    return left

k = 1000 
result = find_first_fibonacci_with_k_digits(k) + 1 
print(f"The first Fibonacci number with {k} digits is F_{result}")

# def fib(n) : 
#     if n==1 or n == 2 :
#         return 1
#     return fib(n-1) + fib(n-2) 

# arr = [ 0, 1 ]
# for i in range( 3 , 1000 ):
#     n = len( arr ) 
#     a = arr[n-1] + arr[n-2] 
#     if( a % 10 == 0 ) :
#         print(i) 
#         print(a)
#     arr.append( a )

