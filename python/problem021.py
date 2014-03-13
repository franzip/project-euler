def sum_divisors(n):
    return sum([x for x in range(1, (n / 2) + 1) if n % x == 0])

def amicable_sum(upper_bound):
    assert type(upper_bound) == int and upper_bound > 0
    amicable = set()
    # check every number from 2 up to upper_bound
    # skip over 1 since it cannot be part of any amicable pair
    for x in range(2, upper_bound):
            amicable_equality = sum_divisors(sum_divisors(x))
            amicable_x = sum_divisors(x)
            # check if f(f(a)) = a and a != b
            if x == amicable_equality and x != amicable_x:
                amicable.add(x)
                amicable.add(amicable_x)
    return sum(amicable)

print amicable_sum(10000)
