def specialTriplet(n): 
    assert type(n) == int  
    upperBound = n / 2   # (a + b + c) / 2 is always bigger than max(a, b, c)
    result = None
    for a in range(upperBound, 1, -1):
        for b in range(a - 1, 1, -1):
            c = (a**2 - b**2)**0.5
            if  a + b + c == n:
                result = int(reduce(lambda x, y: x*y, [a, b, c]))
                x, y, z = b, c, a
    if result:
        return "Triplet (%d + %d + %d) = %d, Product (a*b*c) = %d" %(x, y, z, n, result)
    else:
        return "Cannot find a triplet (a + b + c) = %d" % n
        
print specialTriplet(1000) 