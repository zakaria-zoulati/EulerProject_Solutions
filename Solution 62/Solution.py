a = 1
first = {}
map = {}

while a <= 100_000  :
    arr = []
    b = a**3
    while b > 0:
        arr.append(b % 10)
        b //= 10
    arr.sort()
    seq = "".join(str(item) for item in arr)
    if seq not in map:
        map[seq] = 1
        first[seq] = a
    else:
        map[seq] += 1

    a += 1

n = 1 
while n <= 100_000 :
    arr = []
    b = n**3
    while b > 0:
        arr.append(b % 10)
        b //= 10
    arr.sort()
    seq = "".join(str(item) for item in arr)
    
    if map[seq] == 5 :
        print( n ** 3 ) 
        break 
    n += 1



