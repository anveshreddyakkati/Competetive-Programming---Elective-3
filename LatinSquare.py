# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...
def isLatinSquare(lst):
    a=[]
    h=0
    if len(lst)==len(lst[0]):
        for i in range (len(lst)):
            for j in range (len(lst)):
                
                a.append(lst[i][j])
            break
        # print(a)
        for i in range (len(lst)):
            for j in range (len(lst)):
                # h=lst[i][j]
                # k=lst[j][i]
                # print(h)
                # print("k",k)
                if lst[i][j] in a and lst[j][i] in a:
                    continue
                else:
                    return False
        return True

    # if lst[i][j] in a:
    
print(isLatinSquare([[1,3,3,4],[4,3,2,1],[2,1,4,3],[3,4,1,2]]))



    # Your code goes here...
   
