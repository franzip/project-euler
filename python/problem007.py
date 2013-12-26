from math import ceil

def nthPrime(limit):
    """
    This is a slightly modified version of code used for the Brown University's
    course "Coding the Matrix: Linear Algebra through Computer Science Application"
    """
    assert limit >= 4 and type(limit) == int
    primes = dict()
    # Rough optimization attempt for our Sieve upper bound.
    upperBound = int(ceil(limit**2 / 2.0))   
    a = [True] * upperBound # Initialize the primality list
    a[0] = a[1] = False
    c = 1
    for (i, isprime) in enumerate(a):
        if isprime:
            primes[c] = i
            c += 1
            for n in range(i*i, upperBound, i): # Mark factors non-prime
                a[n] = False
    return primes[limit]


print nthPrime(10001)

