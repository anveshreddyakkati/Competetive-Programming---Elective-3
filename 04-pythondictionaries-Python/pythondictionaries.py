"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores city by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the city listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""


"""Print the following (using "print"). 
1. A list of all city in the USA in
alphabetic order. Make it function with name as sortUSA(), return list of city
2. All city in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this: (Make it function with name as alphaAsia(), return list of city)
1
American City
American City
2
Asian City - Country
Asian City - Country"""


def sortUSA():
    '''Return all the city in the USA in alphabetical order'''
    for a in locations:
        if(a=="North America"):
            #setting as dictionary
            z = dict(locations['North America'])
            for a in z:
                if(a=="USA"):
                    city = z["USA"]
                    city.sort()
    return city
def alphaAsia():    
    '''Return all the city in Asia continent in alphabetical order'''    
    k=[]   
    #creating a list 
    for a in locations:        
        if(a=="Asia"):            
            z=dict(locations["Asia"])            
            for a in z:                
                city=z[a][0] + " - " + a                
                k.append(city)                
                k.sort()
                    
    return k
# Note: Check for test cases to understand the output format.
locations = {'North America': {'USA': ['Mountain View', 'Atlanta']}, 'Asia' : {'India' : ['Bangalore'], 'China' : ['Shanghai']}, 'Africa' : {'Egypt' : ['Cairo']}}