from fractions import gcd

def lcm(a, b):
    return a * (b / gcd(a, b))

def smallestMultiple(n):
    assert n >= 3 and type(n) == int
    sequence = range(1, n + 1)
    def helper(sequence, temp):
        # Reduce the list recursively by taking each time 2 common multiples
        # going from the n-th element to the 1st      
        if len(sequence) == 1:
            return temp
        else:
            return helper(sequence[:-1], lcm(temp, sequence.pop()))
    return helper(sequence, lcm(sequence.pop(), sequence.pop()))
        
print smallestMultiple(20)
