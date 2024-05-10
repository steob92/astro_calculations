from astro_calculations import add, sub, mult, div
import numpy as np

x = 1
y = 2

assert(add(x, y) == 3)
assert(sub(x, y) == 1)
assert(mult(x, y) == 2)
assert(div(x, y) == 0.5)

for i  in range(1, 10):
    assert( add(i,i) == i + i )
    assert( sub(i,i) == i - i )
    assert( mult(i,i) == i * i )
    assert( div(i,i) == i / i )


# Testing numpy arrays
x = np.linspace(1, 10)
y = np.linspace(10, 20)

assert(np.all(add(x, y) == x + y))
assert(np.all(sub(x, y) == x - y))
assert(np.all(mult(x, y) == x * y))
assert(np.all(div(x, y) == x / y))
