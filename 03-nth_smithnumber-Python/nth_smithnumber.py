# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

# def isprime(p):
#     primes=[]
#     if p==2:
#         primes.append(p)
        
#         return True
#     else:
#         for i in range(2,(p//2)+1):
#             if p%i==0:
#                 break
#         else:
#             primefactors.append(p)
            
# def fun_nth_smithnumber(n):
#     l=n
#     k=n
#     v=0
#     x=0
#     a=0
#     if n<10:
#         x=n
#     elif n>9:
#         s=0
#         while(n>0):
#             s=n%10
#             a=a+s
#             n=n//10
        
    
#     for i in range(2,(k//2)+1):
#         if k%i==0 and isprime(i)==True:
#             primefactors.append(i)
#     c=0
#     flag=True
   
        
#     for i in primefactors:
#         flag=True
#         while(flag):        
            
#             if k%i==0 and k!=0:
#                 c=c+i
#                 k=k//i
#             else:
               
#                 flag=False
                
#     b=0
#     q=0
#     for i in primefactors:
#         if i<10:
#             b=b+i
#         else:
#             while(i>0):
#                 q=i%10
#                 b=b+q
#                 i=i//10
                
        
#     if c==l and c!=l:
#         print("cl")
#         #4#false5
#     if c==a:
#         print("ca")#false7,5
#     if a==b and :
#         print("ab")#false7,5,84#true 22,84
#     if c==b:
#         print("cb")#false 5,6,7,10,2311#false5
#     return False
# primefactors=[]
# print(fun_nth_smithnumber(85))




# ///////////////////////////////
from sympy import *

# def isprime(n):
#     if n==1:
#         return False
#     if n==2:
#         return True    
#     for i in range(2, (n//2)+1):
#         if(n%i==0):
#             return False
#     else:
#         return True
# def repeatsum(n):
#     q=0
#     f=0
#     while(n!=0):
#         f=n%10
#         q+=f
#         n=n//10
#     if(q>9):
#         return repeatsum(q)
#     else: 
#         return q        
def smith(n):
    if(isprime(n)!=True):
        k = n
        factors = []
        sumoffactors=0
        sumofnumbers=0
        rem=0
        srem = 0
        stotal = 0
        x =0
        z =0
        ve = 0
        ro = 0
        if n==1:
            return False
        for i in range(2,(n//2) + 1):
            if(isprime(i)==True) and (n%i==0):
                factors.append(i)
         
        for an in str(n):
            ro+=int(an)
       
        li=[]
        for i in factors:
            while (k%i==0 and k!=0):
                li.append(i)    
                sumoffactors+=i
                k=k//i
      
        e = 0        
        for j in li:
            if(j>9):
                for d in str(j):
                    e+=int(d)
            else:
               e+=j
        
        if(ro==e):
            return True
        else:
            return False
def fun_nth_smithnumber(n):
    count=0
    ev=1
    re = 0
    while(n+1!=count):
        if(smith(ev)==True):
            count+=1
            re = ev
        ev+=1
    return re
# print(fun_nth_smithnumber(4))
# print(smith(274))
# print(smith(85))
# print(smith(121))
# print(smith(27))
# print(smith(13))
# print(smith(2))
# print(smith(15))
# print(smith(11))
# print(smith(57))
# print(smith(105))
# print(fun_nth_smithnumber(0))#4
# print(fun_nth_smithnumber(1))#22
# print(fun_nth_smithnumber(2))#27
# print(fun_nth_smithnumber(5))#94
# print(fun_nth_smithnumber(5))#94
# print(fun_nth_smithnumber(6))#94
# print(fun_nth_smithnumber(7))#94
# print(fun_nth_smithnumber(8))#94
# print(fun_nth_smithnumber(9))#94
# print(fun_nth_smithnumber(10))#274
# print(fun_nth_smithnumber(15))#382
# print(fun_nth_smithnumber(17))#438

# print(fun_nth_smithnumber(19))#483


# print(fun_nth_smithnumber(10))
# print(smith(58))
# print(smith(85))
# print(smith(22))
# print(smith(27))
# print(smith(13))
# print(smith(2))
# print(smith(15))
# print(smith(11))
# print(smith(57))
# print(smith(438))
# print(smith(483))
# print(smith(481))