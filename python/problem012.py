import math

def count_factors(n):
    """ 
    Get the number of divisors for an integer.
    """
    result = [1, n]
    for candidate in range(2, int(math.ceil(math.sqrt(n) + 1))):
        if n % candidate == 0:
            result.append(candidate)
            result.append(n / candidate)
    # cast to set in order to avoid counting duplicates
    return len(set(result))
    
def get_triangular(n):
    """
    Get the first triangular number with n divisors
    """
    assert type(n) == int and n > 0
    candidate, offset = 1, 2
    while count_factors(candidate) < n:
        # check only for triangular numbers
        candidate += offset
        offset += 1
    return candidate
  
print get_triangular(500)
