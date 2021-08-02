# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


from sympy import *


def ishappynumber(n):

	
	reminder = 0
	total = 0
    # taking the last digit
	while(n>0):
		reminder = n%10
		total = total +(reminder*reminder)
		n = n//10
	
	if(total==1):
		return True
    #when total >9 checking again whether it will total to 1 or not
	elif(total>9):
		return ishappynumber(total)	
	else:
		return False
# condition to go to the nth position
def fun_nth_happy_prime(n):
    c = 0
    l = 0
    num = 1
    while(c!=n+1):
        if(ishappynumber(num) == True  and isprime(num)):
            c+=1
            l = num
        num = num+1
    return l
