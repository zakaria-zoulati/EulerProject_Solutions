with open( "input.txt" ) as f : 
    names = [ name.strip('"') for name in f.read().split(',') ] 

names.sort()

print( names[0] )

def score( s ) : 
    res = 0
    for c in s : 
        res += ord( c ) - ord( 'A' ) + 1 
    return res

ans = 0  
for i in range( 0 , len( names ) ) : 
    ans += (i+1)*score( names[i] ) 
print( ans )