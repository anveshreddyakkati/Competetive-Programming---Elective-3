# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwith(n):
	n=(n**5)
	for i in range (10):
		if str(i) in str(n):
			continue
		elif(str(i) not in str(n)):
			return False
	return True


def nthwithproperty309(n):
    count=0
    ev=1
    re = 0
    while(n+1!=count):
        if(nthwith(ev)==True):
            count+=1
            re = ev
        ev+=1
    return re
# (0, 309),
# 	(418, 1),
# 	(462, 2),
# 	(474, 3),
# 	(575, 4),
# 	(635, 5),
# 	(662, 6),
# 	(2014, 100),
# 	(7813, 1000)

# print(nthwithproperty309(0))
# print(nthwithproperty309(1))
# print(nthwithproperty309(2))
# print(nthwithproperty309(3))
# print(nthwithproperty309(4))
# print(nthwithproperty309(5))
# print(nthwithproperty309(6))
# print(nthwithproperty309(100))
# print(nthwithproperty309(1000))
# print(nthwithproperty309(0))
# print(nthwithproperty309(0))



