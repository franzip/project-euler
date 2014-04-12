"""
# cheating...

import webbrowser
from itertools import permutations

a = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

for x in range(1, 1000000):
    a.next()
    
print a.next()
webbrowser.open("http://xkcd.com/353/")
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    

def get_nth_perm(iterable, n_perm):
    assert type(iterable) == list or type(iterable) == str
    assert n_perm > 0 and len(iterable) > 0 and  n_perm - 1 < factorial(len(iterable))
    # start counting permutation from 1 (0th perm -> 1st perm)
    n_perm = n_perm - 1
    # cast into a string in each case and force alphanumeric order
    iterable = [str(x) for x in iterable]
    iterable.sort()
    iterable = ''.join(iterable) 
    # set up inloop variables
    inversion_table = []
    index, copy_iter, result = n_perm, [x for x in iterable], ''
    # compute inversion table
    for digits in range(len(iterable) - 1, -1, -1):
        # get the factoradic number sequence for n_perm in inversion_table
        index, quotient = divmod(index, factorial(digits))
        inversion_table.append(index)
        iterable = iterable[:quotient] + iterable[quotient + 1:]
        index = quotient
    # perform shifts and return result    
    for shift in inversion_table:
        result += copy_iter[shift]
        del copy_iter[shift]
    return result
    
print get_nth_perm('0123456789', 1000000)