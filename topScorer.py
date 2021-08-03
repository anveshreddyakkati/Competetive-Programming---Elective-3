# topScorer(data) [10 Points]
# Write the function topScorer(data) that takes a multi-line 
# string encoding scores as csv data for some kind of 
# competition with players receiving scores, so each 
# line has comma-separated values. The first value on 
# each line is the name of the player (which you can 
# assume has no integers in it), and each value after 
# that is an individual score (which you can assume is a 
# non-negative integer). You should add all the scores 
# for that player, and then return the player with the 
# highest total score. If there is a tie, return all the 
# tied players in a comma-separated string with the names 
# in the same order they appeared in the original data. 
# If nobody wins (there is no data), return None (not the 
# string "None"). So, for example:

def topScorer(data):
    
    if (data==""):
        return None
    
    k=[]
    l=[]
    x=data.split("\n")


   
    for i in range (len(x)-1):
        k.append(x[i].split(","))
    # print("k",k)
    for i in range (len(k)):
        # print(k[i][0])
        l.append(k[i][0])
        del k[i][0]
    # print("l",l)
    z=max(k[0])
    # print(z)
    y=max(k[1])
    # print(y)
    # print("l",l)
    # b=str(l[0]+","+l[1])
    # print("b",b)
    if z>y:
        # print(l[0])
        return l[0]
    elif y>z:
        # print(l[0])
        return l[1] 
    else:
        separator = ','
        h=(str(separator.join(l)))
        return h

       
    
     

  
    # Your code goes here...
    
    

data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
assert(topScorer(data) == 'Fred')

data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
assert(topScorer(data) == 'Wilma')

data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
assert(topScorer(data) == 'Fred,Wilma')

assert(topScorer('') == None)
print("All test cases passed...!")
# Hint: you may want to use both splitlines() and split(',') here!
