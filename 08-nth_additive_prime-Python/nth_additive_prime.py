# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2



def fun_nth_additive_prime(n):


	def additiveprime(n):
		k=0
		for i in (str(n)):
			k+=int(i)
		if k==2:
			l.append(n)
			return True
			
		for i in range (2,k):
			if k%i==0:
				return False
			else:
				l.append(n)
				return True


	x=0
	y=0
	l=[]
	while (len(l)!=n):
		y+=1
		additiveprime(y)
		if (len(l)==n):
			print(l[n-1])