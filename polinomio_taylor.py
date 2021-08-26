from sympy import *
import math

# series(expr, n=6, dir='+')

pt = Function('pt')
x = Symbol('x')
fx = cos(x)
interaccion = 6
num_eval = 0

print("Serie de Taylor")
pprint(series(fx, x, n=interaccion))
n = 0
pt = 0
while n < interaccion:
    deriv_fx = fx.diff(x, n)
    deriv_num_eval = deriv_fx.subs(x, num_eval)
    denominador = math.factorial(n)
    siguiente = (deriv_num_eval/denominador)*(x-num_eval)**n
    pt += siguiente
    n += 1

print(N(pt.subs(x, sqrt(2))))


