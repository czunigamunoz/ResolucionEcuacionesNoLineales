from sympy import *

f = lambda x: asin(x)
x = Symbol('x')
fx = asin(x)
a, b = 0.5, 1
n = 5
h = (b - a) / n
intervalo = []


def pasos():
    intervalo.append(a)
    elemento = a + h
    for i in range(n - 1):
        intervalo.append(elemento)
        elemento += h
    intervalo.append(b)


def trapecio_compuesto():
    sumatoria = 0
    for i in range(n - 1):
        sumatoria += f(intervalo[i + 1])
    result = (h / 2) * (f(a) + 2 * (sumatoria) + f(b))
    return N(result, 9)


def integral_evaluada():
    num_integral = integrate(fx, (x, a, b))
    return N(num_integral, 9)


def error(num_metodo, num_integral):
    return N(abs((num_integral - num_metodo) / num_integral) * 100, 3)


if __name__ == '__main__':
    pasos();
    num_metodo = trapecio_compuesto()
    num_integral = integral_evaluada()
    error = error(num_metodo, num_integral)
    print(intervalo)
    print(f"""Numero con trapecio compuesto: {num_metodo}"
Numero integral evaluada: {num_integral}
Error: {error}%""")
