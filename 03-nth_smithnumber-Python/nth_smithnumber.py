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



from sympy import *

def fun_nth_smithnumber(n):
    def isSmith( n) :
        prime=[]
        primes=[]
        
        for i in range (2,(n//2)+1):
            if n%i==0:
                prime.append(i)
        for i in prime:
            if (isprime(i)==True):
                primes.append(i)
        
        inval = n
          
       
        psum = 0
        i=0
        while (i<len(primes)  and primes[i]<= n/2) :
              
            while n % primes[i] == 0 :
                p = primes[i]
                n = n/p
                while p > 0 :
                    psum += (p % 10)
                    p = p//10
            i=i+1
       
        if not n == 1 and not n == inval :
            while n > 0 :
                psum = psum + n%10
                n=n//10
            
      
        insum = 0
        while inval != 0 :
            insum = insum + inval % 10
            inval = inval//10
              
       
        if (psum == insum):
            
            return True
    count=0
    i=1
    while(n+1!=count):  
        if(isSmith(i)==True):
            m=i
            count+=1
        i=i+1
    return m


