def power_digit_sum(n):
    assert type(n) == int or type(n) == long
    return sum([int(digit) for digit in str(n)])
    
print power_digit_sum(2**1000)