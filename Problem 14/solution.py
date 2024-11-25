end = 1000000
curr = 0 
rs = -1 
for i in range( 1,end+1 ) : 
    count = 0 
    ele = i 
    while ele != 1 : 
        count += 1 
        if ele % 2 == 0 : 
            ele /= 2 
        else : 
            ele = 3*ele + 1 
    if count > curr : 
        curr = count 
        rs = i 

print(rs)
