# Write the function bonusFindIntRoots(a,b,c) that takes 
# the int coefficients a, b, c of a quadratic equation of this form:
#      y = ax2 + bx + c
# You are guaranteed the function has 2 real roots, and in fact that 
# the roots are all integers. Your function should return these 2 int roots 
# in increasing order. How does a function return multiple values? Like so:
# return root1, root2

import math
def fun_find_int_roots(a, b, c):
	d1=int((-b+(b**2-4*a*c)**0.5)/2*a)
	d2=int((-b-(b**2-4*a*c)**0.5)/2*a)
	if d1>d2:
		return d2,d1
	else:
		return d1, d2


