def squareDiff(n):
    assert n >= 2 and type(n) == int
    return sum([x for x in range(1, n + 1)])**2 - sum([x**2 for x in range(1, n + 1)]) 
    
print squareDiff(100)