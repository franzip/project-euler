def largestPrime(n):
    assert type(n) == int or type(n) == long
    def helper(n, divisor):
        while divisor != n:
            if n % divisor == 0:
                n /= divisor
            else:
                divisor += 1
        return divisor
    return helper(n, 2)
    
    
print largestPrime(600851475143)