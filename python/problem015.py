def lattice_paths(x, y):
    assert type(x) == int and x > 0 and type(y) == int and y > 0
    return factorial(x + y) / (factorial(x) * factorial(y))

def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)


print lattice_paths(20, 20)
