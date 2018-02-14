player1 = input( "Enter your name player1 : " )
player2 = input( "Enter your name player2 : " )
num = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ]
print (num)
x = int(input( player1 + " choose number from num : "))
while x > 9 or x <= 0 :
    print( " please enter another number : " )
    x = int(input())
num.remove(x)    
print ( num )    
a = int(input( player2 + " choose number from num :"))
while a == x or a >9 or a <= 0  :
    print ( " please enter another number : " )
    a = int(input())
num.remove(a)
print ( num )
y = int(input(player1 + " choose number from num :"))
while y ==x or y == a or y > 9 or y <= 0 :
    print ( " please enter another number : " )
    y = int(input())
num.remove(y)
print ( num )
b = int(input( player2 + " choose number from num : " ))
while b == x or b == a or b == y or b > 9 or b <= 0 :
    print( " please enter anthor number : " )
    b = int(input())
num.remove(b)
print ( num )
z = int(input( player1 + " choose numner from num : "))
while z == x or z == a or z == y or z == b or z > 9 or z <= 0 :
    print ( " please enter another number : " )
    z = int(input())
num.remove(z)
print ( num )
if ( x + y + z ) == 15:
    print ( " the winer is : " + player1)
else:
    c = int(input( player2 + " choose number from num "))
    while c == x or c == a or c == y or c == b or c == z or c > 9 or c <= 0:
        print ( " please enter anothe number : " )
        c = int (input())
    num.remove(c)
    print ( num )
    if ( a + b + c ) == 15:
        print ( " the winer is : " + player2 )
    else:
        g = int(input( player1 + " choose number from num : "))
        while g == x or g == a or g ==y or g == b or g == z or g == c or g > 9 or g <= 0 :
            print ( " please enter another number : " )
            g = int(input())
        num.remove(g)
        print ( num )
        if ( x+ y + z + g ) == 15 :
             print ( " the winer is : " + player1)
        else :
            d = int(input( player2 + " choose number from num : " ))
            while d == x or d == a or d ==y or d == b or d == z or d == c or d == g or d > 9 or d <= 0:
                print ( " please enter another number : " )
                d = int(input())
            num.remove(d)
            print ( num )
            if ( a + b + c + d ) == 15 :
                print ( " the winer is : " + player2 )
            else :
                h = int(input( player1 + " choose number from num : " ))
                while h == x or h == a or h == y or h == b or h == z or h == c or h == g or h == d or h > 9 or h <= 0 :
                      print ( " please enter another number : " )
                      h = int(input())
                num.remove(h)
                print ( num )
                if ( x + y + z + g + h ) == 15 :
                     print ( " the winer is : " + player1)
                else :
                    print ( " the game is draw " )
                    print ( " try again " )
                    
                    
                
             
            
        
            
        
        
    
