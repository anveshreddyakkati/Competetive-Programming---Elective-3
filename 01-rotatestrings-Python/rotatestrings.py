# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	#enters when n>0

	if n>0:
		n = n-len(s)
		s = s[n:] + s[:n]
		return s
	#when nis between 0 and -len(s)

	
	elif(n<0 and abs(n)<=len(s)):
		s = s[len(s)+n:] + s[:len(s)+n]
		return s
	#enters when nis outside the range of len(s)	
		
	else:
		

		n = n+len(s)
		s = s[len(s)+n:] + s[:len(s)+n]
		return s
