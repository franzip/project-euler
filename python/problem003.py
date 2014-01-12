def find_largest_factor(prime):
    assert type(prime) == int or type(prime) == long
    # helper function
    def helper(prime, divisor):
        # check for divisors starting from 2
        while prime != divisor:
            if prime % divisor == 0:
                prime /= divisor
            else:
                divisor += 1
        return divisor
    # seed helper with 2    
    return helper(prime, 2)
    
    
print find_largest_factor(600851475143)