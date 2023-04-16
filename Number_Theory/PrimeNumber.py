#using Sieve of Eratosthenes algorithm to find prime number 
# Python program to print all primes smaller than or equal to 
# n using Sieve of Eratosthenes 
  
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n+1): 
        if prime[p]: 
            print(p)

# Python program to print prime factors 
  
import math 
  
# A function to check prime factors of  
# a given number n 
def checkPrime(n): 
    if n<2:
        return False
    if n == 2 and n ==3:
        return True
    # Print the number of two's that divide n 
    if n % 2 == 0: 
        return False
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2):  
        if n%i == 0:
            return False
    return True

# driver program 
if __name__=='__main__': 
    n = 315
    print("Following are the prime numbers smaller")
    print( "than or equal to", n )
    SieveOfEratosthenes(n) 
    t = 311
    print(checkPrime(t))