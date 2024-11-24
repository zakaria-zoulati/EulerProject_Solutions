tar = 600851475143
max = 1 
for i in range(2,tar) : 
    if tar % i == 0 : 
        max = i 
        while tar % i == 0 : 
            tar /= i 
        
    if tar == 1 :
        break 
print(max)
        