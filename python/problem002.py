def sum_even_fibo(upper_bound):
    assert type(upper_bound) == int or type(upper_bound) == long
    add_fibo = 0
    fibo, increment = 1, 0
    # generate fib numbers on the fly from 0 to upper_bound
    while fibo < upper_bound: 
        fibo, increment = fibo + increment, fibo
        if fibo % 2 == 0:
            add_fibo += fibo
    return add_fibo
    
print sum_even_fibo(4000000)
        
        

