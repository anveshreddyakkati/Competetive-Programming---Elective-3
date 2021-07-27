# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
    # your code goes here
    cha = 0
    tin = 0
    jo = 1
    while jo<len(a):
        if(a[jo] < a[jo-1]):
            cha = 1
        elif(a[jo] > a[jo-1]):
            tin = 1    
        jo+=1
   #checking for one to be false
   #then returning true
    if(not cha or not tin):
        return True
    else:
        return False