# Write the function happynumber(q) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(happynumber(1) == 1)
# assert(happynumber(2) == 7)
# assert(happynumber(3) == 10)
# assert(happynumber(4) == 13)
# assert(happynumber(5) == 19)
# assert(happynumber(6) == 23)
# assert(happynumber(7) == 28)
# assert(happynumber(8) == 31)


# def happynumber(q):
#     #convert negative number to positive
#     q=abs(q)
#     a=0
    
#     #converting to the list
#     x=list(("".join((i) for i in (str(q)))))
#     # print("x",x)
#     #checking the length
#     if (len(x)==1):
#         if q in range (2,7):
#             print(q)
#             # print(l)
#         elif q in range(8,10):
#             print(q)
#         elif q==0:
#             print(q) 
#         else:
#             l.append(z)
#             # print(l)
#             print(q)
#     #checking for more than 9
#     else:
#         for i in range(len(x)):
#             k=int(x[i])
#             a+=k*k
#             # print("a",a)
            
#         if a==1:
#             l.append(z)
#             # print(l)
#             return q
#         else:
#             return happynumber(a)
# # print(nth-_happy_number(23))


# l=[]
# i=0
# while (len(l)!=3):
#     i+=1
#     z=i
    
#     print(happynumber(i))
#     # print (l[0])
    


   

def nth_happy_number(n):


    m=[1,7]
    a=0

    def happynumber(q):
        #convert negative number to positive
        q=abs(q)
        a=0
        
        #converting to the list
        x=list(("".join((i) for i in (str(q)))))
        # print("x",x)
        #checking the length
        if (len(x)==1):
            if q in (m):
                l.append(z)
                
                # print(l)
            
                
            # else:
            #     continue
                # l.append(z)
                # print(l)
                
        #checking for more than 9
        else:
            for i in range(len(x)):
                k=int(x[i])
                a+=k*k
                # print("a",a)
                
            if a==1:
                l.append(z)
                # print(l)
                return z
            else:
                return happynumber(a)
    # print(nth-_happy_number(23))


    l=[]
    i=0
    while (len(l)!=n):
        i+=1
        z=i
        happynumber(i)
        if len(l)==n:
            return (l[n-1])
