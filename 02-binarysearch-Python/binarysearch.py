"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    lowvalue = 0 # lowvalue
    highvalue = len(input_array)-1 # highvalue

    while lowvalue <= highvalue:
  
        middle = lowvalue + (highvalue - lowvalue) // 2 #calulating the middle value of the array
          
        if input_array[middle] == value:
            return middle
  
        elif input_array[middle] < value: # if middle value is less than the given value we will ignore the left half of the middle value 
            lowvalue = middle + 1

        else:
            highvalue = middle - 1 # if middle value is greater than the given value we will ignore the right half of the middle value
      
    return -1