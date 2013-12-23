def isPal(n):
    return n == n[::-1]
    
def maxPalindrome(ndigits):
    assert type(ndigits) == int and ndigits > 1
    pal = 0
    upperBound = 10**ndigits - 1
    # Raw attempt of optimization by reducing the loop lower bound (epsilon).
    # Should return a result in a reasonable time for ndigits <= 5
    if ndigits <= 3:
        epsilon = upperBound - upperBound//10
    else:
        epsilon = upperBound - upperBound//100
    for x in range(upperBound, epsilon, -1):
        for y in range(upperBound, epsilon, -1):
            if isPal(str(x * y)) and x * y > pal:
                pal = x * y
    return pal

print maxPalindrome(3)

