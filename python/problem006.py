def sum_square_diff(n):
    assert n >= 2 and type(n) == int
    # return (1 + 2 + ... + n)^2 - (1^2 + 2^2 + ... + n^2)
    return sum([x for x in range(1, n + 1)]) ** 2 -     \
           sum([x ** 2 for x in range(1, n + 1)]) 
    
print sum_square_diff(100)
