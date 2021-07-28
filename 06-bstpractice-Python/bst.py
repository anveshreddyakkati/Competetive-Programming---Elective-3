class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        # checking whether it has root or not 
        newNode = Node(new_val)
        if (self.root == None):
            self.root = newNode
            #i\f it ha s root 
        else:
            current = self.root
            parent = self.root
            while (current != None):
                parent = current
                #if new value less than current
                if (new_val < current.value):
                    current = current.left
                    #if new value greater than current
                else:
                    current = current.right
            if (new_val < parent.value):
                parent.left= newNode
            else:
                parent.right = newNode

    def printSelf(self):
        # Your code goes here
        # printing root
        print(self.root)


        
    def search(self, find_val):
        # Your code goes here
        # finding the value
        while self.root!=None:
            if self.root.value == find_val:
                return True 
            # if we are at the required root
            if self.root.value < find_val:
                self.root = self.root.right
                # if we are at the required root or not
            else:
                self.root = self.root.left
        return False

