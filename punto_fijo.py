from sympy import *

fx = Function('fx')
gx = Function('gx')
x = Symbol('x')

fx = 2**(-x)
gx = sqrt(exp(exp(3*x)-30)-1)

# x_0 = El entero siguiente al limite inferior del intervalo de la |derivada gx| < 1
x_0 = 1.1337322461
i = 0
while True:
    siguiente = N(fx.subs(x, x_0), 5)
    print(f"X{i+1} = {x_0} \t g(X{i}) = {siguiente}")
    if str(x_0) == str(siguiente):
        break
    x_0 = siguiente
    i += 1
