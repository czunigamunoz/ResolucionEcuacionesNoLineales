from sympy import *

f = lambda x: asin(x)
x = Symbol('x')
fx = asin(x)
a, b = 0.5, 1


def integral_evaluada():
    num_integral = integrate(fx, (x, a, b))
    return N(num_integral, 9)


def error(num_metodo, num_integral):
    return N(abs((num_integral-num_metodo)/num_integral)*100, 3)


def trapecio():
    return N((b-a)*((f(a) + f(b))/2), 9)


if __name__ == '__main__':
    num_metodo = trapecio()
    num_integral = integral_evaluada()
    error = error(num_metodo, num_integral)
    print(f"""Numero con trapecio compuesto: {num_metodo}
    Numero integral evaluada: {num_integral}
    Error: {error}%""")
