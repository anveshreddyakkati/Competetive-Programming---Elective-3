# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.
#We can determine from their equations whether two lines 
# are parallel by comparing their slopes. If the slopes are the 
# same and the y-intercepts are different, the lines are parallel. 
# If the slopes are different, the lines are not parallel. Unlike parallel lines,
#  perpendicular lines do intersect.


def lineintersection(m1, b1, m2, b2):
	# your code goes here
	#if lenes are parallel or identical
	if(m1==m2 or b1==b2 or m1%m2==0 or m2%m1==0):
		return None
	else:
		return (b2-b1)/(m1-m2)

