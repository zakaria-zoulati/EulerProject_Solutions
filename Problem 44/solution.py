import math

def is_pentagonal(n):
    if n <= 0:
        return False
    test = (1 + math.sqrt(1 + 24 * n)) / 6
    return test == int(test)

def generate_pentagonals(limit):
    pentagonals = set() 
    n = 1
    while True:
        p = n * (3 * n - 1) // 2
        if p >= limit:
            break
        pentagonals.add(p)
        n += 1
    return pentagonals

limit = 10000000  # To adjust each Time till get a result
pentagonals = generate_pentagonals(limit)

min_diff = float('inf')
result_j = 0
result_k = 0


for j in pentagonals:
    for k in pentagonals:
        if j < k: # Small Optimisation
            sum_jk = j + k
            diff_jk = k - j
            if sum_jk in pentagonals and diff_jk in pentagonals:
                if diff_jk < min_diff:
                    min_diff = diff_jk
                    result_j = j
                    result_k = k
                    

print(f"j: {result_j}")
print(f"k: {result_k}")
print(f"k - j: {min_diff}")