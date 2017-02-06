import math 

def primeGenerator(n):


     sieve = [True] * n #Not sure if the best way to implement asked around a lot of groups

     sieve[0] = sieve[1] = False #solution to save 1 second


 

     for i in range(2, int(math.sqrt(n)) + 1):

         num = i * 2

         while num < n:

             sieve[num] = False

             num += i



     # compile the list of primes

     primes = []

     for i in range(n):

         if sieve[i] == True:

             primes.append(i)
             



     return primes

