from astro_calculations import add, sub, mult, div

x = 1
y = 2

assert(add(x, y) == 3)
assert(sub(x, y) == -1)
assert(mult(x, y) == 2)
assert(div(x, y) == 0.5)

for i  in range(1, 10):
    assert( add(i,i) == i + i )
    assert( sub(i,i) == i - i )
    assert( mult(i,i) == i * i )
    assert( div(i,i) == i / i )