# Write the function nearestBusStop(street) that takes x 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	for i in range(street+1):
		#starting point
		x = i*8
		#ending point
		y = (i+1)*8
		#highest return
		if(abs(street-x)<=8 and abs(street-y)<=8):
			if((abs(street-x) > abs(street-y))):
				return y
				#lowest return
			elif((abs(street-x) == abs(street-y)) or (abs(street-x) < abs(street-y))):
				return x
