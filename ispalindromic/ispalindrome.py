def isPalindromicPrime(n):
    if n==2:
        return True
    def prime(k):
        k=int(k)
        for i in range(2,(k//2)+1):
            if k%i==0:
                return False
        return True 
    n=str(n)
    if(n==n[::-1]) and prime(int(n))==True:
        return True
    else:
        return False
    

assert (isPalindromicPrime(2) == True)
assert (isPalindromicPrime(10) == False)
assert (isPalindromicPrime(104) == False)
assert (isPalindromicPrime(235) == False)
assert (isPalindromicPrime(131) == True)
assert (isPalindromicPrime(900) == False)
assert (isPalindromicPrime(101) == True)
assert (isPalindromicPrime(383) == True)
# assert (isPalindromicPrime(373) == True)
assert (isPalindromicPrime(121) == False)
print("All test cases passed... :-)")