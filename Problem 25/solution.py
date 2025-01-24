import math

def fibonacci_digits(k):
    phi = (1 + math.sqrt(5)) / 2
    return math.floor(k * math.log10(phi) - math.log10(math.sqrt(5))) + 1

def find_first_fibonacci_with_k_digits(k):
    left, right = 1, 10000  
    while left < right:
        mid = left + (right - left) // 2
        if fibonacci_digits(mid) < k:  
            left = mid + 1
        else:  
            right = mid
    return left

k = 1000 
result = find_first_fibonacci_with_k_digits(k) 
print(f"The first Fibonacci number with {k} digits is F_{result}")


