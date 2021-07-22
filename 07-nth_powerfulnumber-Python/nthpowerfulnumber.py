# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every isprimenumber factor p of it, p2 also divides it. 
# For example:- 36 is z powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math

#checking for prime number
def isprimenumber(n):
	#as 2 prime
		if(n==2):
				return True
		else:
			#checks other than 1 and 2
    			for i in range(2,int(n/2)+1):
    					if(n%i==0):
    							return False
		return True
#checks powerful
def powerfull(n):
	# as 1 powerfull
		if(n==1):
			return True
		else:
			count=0
			count1=0
			#checking the rules of i and i*i
			for i in range(2,int(n/2)+1):
						if(n%i==0 and isprimenumber(i)):
								count+=1
								if(n%(i*i)==0):
									count1+=1
						print(count)
						print(count1)
			# if not multiple by i and i*i
			if(count==0 or count1==0):
					return False
			# if multiple by i and i*i
			elif(count==count1):
					return True
		return False
	
def nthpowerfulnumber(n):
	
	flag=True
	cnum=1
	count=0
	while(flag):
		if(powerfull(cnum)):
			# if we found the nth
			if(n==count):
						flag=False
						return cnum
		#if powerfull but not required
			cnum+=1
			count+=1
		# if we dont found the nth
		else:
			cnum+=1
