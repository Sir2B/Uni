def adder(x):
    return lambda y: x + y
add5 = adder(5)
print add5(1)
