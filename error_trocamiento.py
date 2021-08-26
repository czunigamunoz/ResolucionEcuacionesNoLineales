from sympy import *

'''
series(expr, x=None, x0=0, n=6, dir='+')
'''

x = Symbol('x')
fx = exp(x)


def error_troncamiento(repeticiones, evaluar):
    gx = 0
    interaccion = 0
    valor_anterior = 0
    while interaccion < repeticiones:
        print(f"Interaccion: {interaccion + 1}")
        print("Serie de Taylor")
        pprint(series(fx, x, n=interaccion+1))
        valor = (fx.diff(x, 0).subs(x, 0) / factorial(interaccion)) * x ** interaccion
        gx += valor
        valor = gx.subs(x, evaluar)
        print(f"Valor evaluado en la serie de Taylor: {valor}")
        error = float(((valor - valor_anterior) / valor) * 100)
        print(f"Error: {error}%")
        print("-----------------------------------------------------")
        valor_anterior = valor
        interaccion += 1


num = int(input("Digite numero de repeticiones: "))
num_evaluar = int(input("Digite el valor para reemplazar en la funcion: "))
error_troncamiento(num, num_evaluar)
