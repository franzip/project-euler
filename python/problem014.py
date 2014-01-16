def get_collatz_length(n):
    result = []
    # optimized algorithm for collatz length
    # still pretty slow, longest_collatz(1000000) take over 40s
    while n != 1:
        # handle odd elements in the sequence
        if n % 2:
            if n % 4 == 1:
                # 3n + 1 is part of the 4n + 1 sequence
                n = 3 * ((n - 1) / 4) + 1          
            else:
                # if n is odd, 3n + 1 will always be even, thus divide by 2
                n = (3 * n + 1) / 2                              
        # handle even elements in the sequence
        else:
            if n % 4:
                # apply ordinary algorithm for even numbers not divisible by 4
                n /= 2    
            else:
                # dividing by 4 let us skip at least 1 step in the worst case
                n /= 4
        # add n to the sequence            
        result.append(n)
            
    return len(result)

def longest_collatz(upper_bound):
    assert type(upper_bound) == int and upper_bound > 0
    longest = None
    # get the integer in (1 ... upper_bound) which generates the longest collatz chain
    for x in range(1, upper_bound + 1):
        collatz_length = get_collatz_length(x)
        if collatz_length > longest:
            longest = x
    return longest
    
print longest_collatz(1000000)
