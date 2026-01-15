
grid = []

with open( "input.txt" ) as f :
    for line in f : 
        row = list( map( int , line.split() ) )
        grid.append( row )


for i in range( 1 , 100 ) : 
    for j in range( 0 , i+1 ) : 
        grid[i][j] += max( grid[i-1][j-1] if j>0 else 0 , grid[i-1][j] if i !=j else 0 )

ans = 0 
for i in range( 0 , 100 ) : 
    ans = max( ans , grid[99][i] )

print( ans )