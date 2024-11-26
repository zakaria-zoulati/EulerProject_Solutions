a = 1 << 1000
print(a)
sum = 0
while a != 0:
    r = a % 10
    sum += r
    a //= 10  
print(sum)
