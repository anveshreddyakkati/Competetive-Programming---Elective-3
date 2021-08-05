# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




from math import factorial
def fun_pascaltrianglevalue(row, col):
    if (row>=col):
        r=[]
        for i in range(row+1):
            l=[]
 
            for j in range(i+1):
                l.append(factorial(i)//(factorial(j)*factorial(i-j)))
            r.append(l)

        return (r[row][col])
    else:
        return 0