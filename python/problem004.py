def is_palindrome(n):
    return n == n[::-1]
    
def max_palindrome_for(n_digits):
    assert type(n_digits) == int and n_digits > 1 
    largest_palindrome = 0
    found = False
    upper_bound = (10**n_digits) - 1
    # Attempt of optimization by setting a loop lower bound.
    # Should return a result in a reasonable time for n_digits <= 8
    if n_digits <= 3:
        lower_bound = upper_bound - (upper_bound // 10)
    else:
        lower_bound = upper_bound - (upper_bound // 100)      
    # check all pairs from upperbound to lowerbound    
    for x in range(upper_bound, lower_bound, -1):
        if found:
            break
        for y in range(upper_bound, lower_bound, -1):
            if is_palindrome(str(x * y)) and not found:
                largest_palindrome = x * y
                found = True
    return largest_palindrome

print max_palindrome_for(3)
