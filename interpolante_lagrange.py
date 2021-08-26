from sympy import *

px = Function('px')
px = 0
x = Symbol('x')
x_i = [0, 0.2, 0.4]
y_i = [3.59, 3.11, 3.08]

for i in range(len(y_i)):
    numerador = 1
    denominador = 1
    for j in range(len(x_i)):
        if i != j:
            numerador *= (x - x_i[j])
            denominador *= (x_i[i] - x_i[j])
        termino = (numerador / denominador) * y_i[i]
    px += termino

print(expand(px))
