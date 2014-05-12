def lattice_paths(n_grid):
    assert type(n_grid) == int and n_grid > 0
    return factorial(2 * n_grid) / factorial(n_grid)**2
    
def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)

            
print lattice_paths(20)
