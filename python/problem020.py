def factorial_digit_sum(n):
    assert type(n) == int and n >= 0
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    return sum([int(x) for x in str(factorial(n))])
    
print factorial_digit_sum(100)