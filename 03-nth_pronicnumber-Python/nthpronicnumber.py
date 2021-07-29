# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).




def nthpronicnumber(n):
	if n==0:
		return 0
	if n==1:
		return 2
	else:
		return (n)*(n+1)

	