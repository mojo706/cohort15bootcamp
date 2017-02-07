"""
This is simpler code to improve testability(sp) still working on the other one though
Feel free to offer improvements 
"""
def primeGen(start, end):
    primes = list()
    if start <= 1:
        start = 2

    sieve = [True] * (end + 1) # really fast just not sure about massive numbers though
    for p in range(start, end + 1):
        if (sieve[p]):
            primes.append(p)
            for i in range(p, end + 1, p):
                sieve[i] = False
    return primes
# print(primeGen(0, 1000)) Uncomment to test
