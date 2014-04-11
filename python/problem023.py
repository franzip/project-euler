import math 

def check_abundant(n):
    # skip duplicate checks with set()
    divisors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            divisors.add(i)
            rest = n / i
            if rest != n:
                divisors.add(rest)
    try:
        # check for the sum of n divisors -> 1 + sum {a, b, ... n / 2} > n
        return 1 + reduce(lambda x, y: x + y, divisors) > n
    except:
        # n is prime, hence return false
        return False
        
def non_abundant_sum(upper_bound):
    assert type(upper_bound) == int
    # get all abundant in the range
    abundant_set = {x for x in range(1, upper_bound + 1) if check_abundant(x)}
    def check_abundant_sum(n, abundant_set):
        # if m is abundant, and (n - m) is also abundant, then n is (m + (n - m))
        for abundant in abundant_set:
            if (n - abundant) in abundant_set:
                return True
        return False

    # return all positive integers which can't be written as sum of an abundant pair
    return sum([x for x in range(1, upper_bound + 1) 
                if not check_abundant_sum(x, abundant_set)])

print non_abundant_sum(28123)
