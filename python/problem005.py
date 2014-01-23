from fractions import gcd

def lcm(a, b):
    return a * (b / gcd(a, b))

def smallest_multiple(upper_limit): 
    assert upper_limit >= 3 and type(upper_limit) == int
    # save the sequence as a list
    sequence = range(1, upper_limit + 1)
    def helper(sequence, accumulator):
        # use tail recursion and return the least common multiple
        # maximum recursion depth triggers for upper_limit > 961
        if len(sequence) == 1:
            return accumulator
        else:
            return helper(sequence[:-1], lcm(accumulator, sequence.pop()))
    return helper(sequence, lcm(sequence.pop(), sequence.pop()))
        
print smallest_multiple(20)
