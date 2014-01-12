def find_abc_product(abc_sum):
    """
    abc_sum is (a + b + c) where a, b, c are any positive integers
    Returns (a * b * c) if abc_sum represents the sum of a pythagorean triplet
    """ 
    assert type(abc_sum) == int and abc_sum > 0
    # given a pythagorean triplet (a, b, c)
    # (a + b + c) / 2 is always bigger than max(a, b, c)
    # hence start the outer loop from n / 2
    upper_bound = abc_sum / 2   
    triplet_product = None
    for a in range(upper_bound, 1, -1):
        for b in range(a - 1, 1, -1):
            # get the third term for the triplet
            c = (a ** 2 - b ** 2) ** 0.5
            # if the pythagorean triplet match the input n, compute the product
            if  a + b + c == abc_sum:
                triplet_product = int(reduce(lambda x, y: x * y, [a, b, c]))
                x, y, z = b, c, a
    if triplet_product:
        return "Pythagorean Triplet (%d + %d + %d) = %d\nProduct (a * b * c) = %d"     \
                 %(x, y, z, abc_sum, triplet_product)
    else:
        return "Cannot find a triplet (a + b + c) = %d" % abc_sum
        
print find_abc_product(1000) 

