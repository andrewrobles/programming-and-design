def gcdRecur(a, b):
    '''
    a & b are positive numbers
    a = the base number
    b = the exponent
    
    returns the greatest common divisor of a & b
    '''


    if b == 0:      #base case returns the 
        return a
    else:
        return gcdRecur(b, a%b) #recursive case

a = 7
b = 84


print(gcdRecur(a, b))