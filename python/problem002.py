def fib(upperBound):
    assert type(upperBound) == int
    sumEvenFibo = 0
    fibo, increment = 1, 0
    while fibo < upperBound:
        fibo, increment = fibo + increment, fibo
        if fibo % 2 == 0:
            sumEvenFibo += fibo
    return sumEvenFibo
    
print fib(4000000)
        
        

