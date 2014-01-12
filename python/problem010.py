def primes(limit):
    """
    Code used for the Brown University's course "Coding the Matrix: Linear Algebra 
                through Computer Science Application"
    """
    assert type(limit) == int
    primeset = set()
    # Initialize the primality list
    a = [True] * limit
    a[0] = a[1] = False
    for (i, is_prime) in enumerate(a):
        if is_prime:
            primeset.add(i)
            for n in range(i * i, limit, i): 
                # Mark factors non-prime
                a[n] = False
    return primeset
    
print sum(primes(2000000))