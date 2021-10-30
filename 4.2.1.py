def gcdIter(a,b):   #defines the funtion
    """
    finds the greatest common denominator between
    2 variables
    """

    if b<a:         #starts the loop
        a,b = b,a   #????
    c = a           #
    while c>0:      #starts the loop if c is > 0
        if (a/c==a//c) and (b/c==b//c): #?????
            return c
        c-=1 

a = 91

b = 260


print(gcdIter(a,b))