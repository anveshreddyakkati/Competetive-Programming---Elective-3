# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	if (row>=col):
		r=[]
		for i in range (1,row+1):
			t=[]
			for i in range (1,i+1):
				t.append(i)
			r.append(t)

		return (r[row-1][col-1])
	else:
		return 0