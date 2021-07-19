# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 


def fun_set_kth_digit(n, k, d):
    if n>0:

        x=[str(i) for i in str(n)]
        y=x[::-1]
        b=len(x)
        if k<(b):
            y[k]=d
            x=y[::-1]
            f=int("".join([str(i) for i in x]))
            return f
        else:            
            c=int(str(d)+str(n))        
            return c
    else:
        n=abs(n)
        x=[int(i) for i in str(n)]        
        b=len(x)
        if k>=(b):     
            
            f=("".join([str(i) for i in x]))
            g=int(str("-")+str(d)+str(f))
            return g



