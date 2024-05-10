from astro_calculations import add, sub, mult, div, capped_sqrt
import numpy as np

x = 1
y = 2

assert(add(x, y) == 3)
assert(sub(x, y) == -1)
assert(mult(x, y) == 2)
assert(div(x, y) == 0.5)
assert(capped_sqrt(x) == 1)

for i  in range(-10, 10):
    if i == 0:
        continue
    assert( add(i,i) == i + i )
    assert( sub(i,i) == i - i )
    assert( mult(i,i) == i * i )
    assert( div(i,i) == i / i )
    assert( capped_sqrt(x) == np.sqrt(x) if x > 0 else 0 )


# Testing numpy arrays
x = np.linspace(-10, 10)
y = np.linspace(10, 20)

assert(np.all(add(x, y) == x + y))
assert(np.all(sub(x, y) == x - y))
assert(np.all(mult(x, y) == x * y))
assert(np.all(div(x, y) == x / y))
assert(capped_sqrt(x) == np.array([np.sqrt(x) if x > 0 else 0]))
