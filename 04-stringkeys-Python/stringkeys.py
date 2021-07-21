"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        # Hash Value = (ASCII Value of First Letter * 100) + 
        # ASCII Value of Second Letter 
        # Your code goes here
        # to store the string at
        #  the hash value of string
        hv = self.calculate_hash_value(string)
        self.table[hv] = string
        
    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        # Your code goes here
        #to find the string in 
        # table and pass it to hash 
        #function
        if string in self.table :
            return self.calculate_hash_value(string)
        else:
            return -1
        
    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        # Your code goes here
        #to calculate hash value of 
        # the strinf
        hv = (ord(string[0])*100) + ord(string[1])
        return hv

