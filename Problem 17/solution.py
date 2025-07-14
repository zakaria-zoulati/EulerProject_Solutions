m = { }
m[ 0 ] = 0 
m[ 1 ] = 3
m[ 2 ] = 3 
m[ 3 ] = 5
m[ 4 ] = 4 
m[ 5 ] = 4 
m[ 6 ] = 3
m[ 7 ] = 5 
m[ 8 ] = 5 
m[ 9 ] = 4 
m[10] = 3 
m[11] = 6 
m[12] = 6
m[13] = 8 
m[14] = len( "fourteen" ) 
m[15] = len( "fifteen" )
m[16] = len( "sixteen" )
m[17] = len( "seventeen" )
m[18] = len( "eighteen" )
m[19] = len( "nineteen" )
m[20] = len( "twenty" )
m[30] = len( "thirty" )
m[40] = len( "forty" )
m[50] = len( "fifty" )
m[60] = len( "sixty" )  
m[70] = len( "seventy" )
m[80] = len( "eighty" )
m[90] = len( "ninety" )

for i in range( 21 , 100 ) :
    if i % 10 != 0 : 
        m[i] = m[(i//10)*10] + m[i%10]


a = len( "hundred" )
for i in range( 100 , 1000 ) :
    m[i] = m[i//100] + a 
    if i % 100 != 0 : 
        m[i] += 3 + m[i%100] 


m[1000] = len( "onethousand" )


rs = 0 
for i in range( 1 , 1001 ) :
    rs += m[i] 


print(rs)