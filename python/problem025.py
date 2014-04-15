def fib_generator():
    # set up a fibonacci number generator
    x, y = 0, 1
    yield 0
    while True:
        x, y = y, x + y
        yield x
        
def nth_fibonacci_term(n_digit):
    assert type(n_digit) == int and n_digit > 0
    fib = fib_generator()
    result = 0
    def fib_memo(x, cache):     
        assert type(x) == int and x >= 0 and type(cache) == dict
        # use caching
        if x in cache:
            return cache[x]
        result = fib.next()
        cache[x] = result
        return result
    # keep rolling fibonacci numbers until threshold
    while len(str(fib_memo(result, {}))) < n_digit:
        result += 1
    return result
    
print nth_fibonacci_term(1000)
    