from math import ceil

def find_nth_prime(n):
    """
    This is a slightly modified version of code used for the Brown University's
    course "Coding the Matrix: Linear Algebra through Computer Science Application"
    """
    assert n >= 4 and type(n) == int
    primes = dict()
    # Rough optimization attempt for our Sieve upper bound.
    upper_bound = int(ceil(n ** 2 / 2.0))  
    # Initialize the primality list 
    a = [True] * upper_bound 
    a[0] = a[1] = False
    c = 1
    for (i, is_prime) in enumerate(a):
        if is_prime:
            primes[c] = i
            c += 1
            for x in range(i * i, upper_bound, i): 
                # Mark factors non-prime
                a[x] = False
    return primes[n]


print find_nth_prime(10001)
