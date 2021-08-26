from sympy import *

"""
Funcion f(x) = arctan(x) + x - 1
Intervalo [0,1]
Tolerancia = 0.005
"""

x = Symbol('x')
# fx = atan(x)+x-1
fx = x ** 5 - 100 * x ** 4 + 3995 * x ** 3 - 79700 * x ** 2 + 794004 * x - 3160075
# a, b = 0, 1
a, b = 17, 22.2
tol = 0.005

"""
Funcion Continua
lim x->c f(x) existe
f(c) existe
lim x->c f(x) = f(c)
"""


def fun_continua(num):
    resp1 = limit(fx, x, num)
    resp2 = fx.subs(x, num)
    return True if resp1 == resp2 else False


def signos_opuestos(num1, num2):
    return True if (num1).is_positive != (num2).is_positive else False


'''
Verificar si la funcion es continua y 
si la funcion evaluada en los extremos tiene signos opuestos

'''
continua = fun_continua(a) and fun_continua(b)
signos = signos_opuestos(fx.subs(x, a), N(rad(deg(fx.subs(x, b))), 4))
if continua and signos:
    i = 0
    while True:
        num1 = fx.subs(x, a)
        # num2 = N(rad(deg(fx.subs(x,b))), 4)
        num2 = fx.subs(x, b)
        p = N(a - (fx.subs(x, a) * (b - a)) / (fx.subs(x, b) - fx.subs(x, a)), 4)
        if abs(b - a) < tol:
            print(p)
            break
        i += 1
        nuevoLimite = fx.subs(x, p)
        tempB = b
        if num1 * nuevoLimite < 0:
            b = p
        elif num1 * nuevoLimite > 0:
            a = p
        error = abs(((b - tempB) / b)) * 100
        print(f"Interaccion N: {i}")
        print(f"Intervalo desde: {a} -- hasta: {b} con un error de: {error}%")
        if error == 0:
            print(f"EXITO Raiz aproximada es X = {b} en la interaccion: {i}")
            break
else:
    print(f"Continua: {continua} -- Signos opuestos: {signos} ")
