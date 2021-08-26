from sympy import *

fx = Function('fx')
x = Symbol('x')

fx = (1 / exp(x)) + x - 2
x_0 = 1
i = 0
while True:
    siguiente = N(x_0 - (fx.subs(x, x_0) / diff(fx, x).subs(x, x_0)), 6)
    print(f"X{i + 1} = {siguiente} --- X{i} = {x_0}")
    if str(x_0) == str(siguiente):
        break
    x_0 = siguiente
    i += 1
