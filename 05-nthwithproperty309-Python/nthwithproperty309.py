# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	n=(n**5)
	for i in range (10):
		if str(i) in str(n):
			continue
		elif(str(i) not in str(n)):
			return False
	return True

count=0
s=1
while ( n != count):

