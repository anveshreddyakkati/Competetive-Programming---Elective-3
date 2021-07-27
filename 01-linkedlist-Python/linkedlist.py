"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        new_element = Element(new_element)
        temp = self.head
        if self.head:
            while temp.next:
                temp = temp.next
            temp.next = new_element
        else:
            self.head = new_element

            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        temp = self.head
        count = 1
        if(position<1):
            return None
        while(temp and count<=position):
            if(count == (position)):
                # print("s:", temp.value)
                return temp.value
            count +=1
            temp = temp.next
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        if position == 1:
            new_node = Element(new_element)
            new_node.next = self.head
            self.head = new_node
        i = 1
        n = self.head
        while i < position-1 and n is not None:
            n = n.next
            i = i+1
        if n is not None:
            new_node = Element(new_element)
            new_node.next = n.next
            n.next = new_node

    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp = self.head
        beforenode = None

        while(temp.next and temp.value!=value):
            beforenode = temp
            temp=temp.next
        if(temp.value == value):
            if(beforenode):
                beforenode.next = temp.next
            else:
                self.head=temp.next




