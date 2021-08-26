import math


def f(x):
    return math.sin(x)


def f_d(x):
    return math.cos(x)


x_0 = 2
h = 0.1
num_derivada = f_d(x_0)


def adelante():
    return (-3*f(x_0) + 4*f(x_0+h) - f(x_0+2*h))/2*h


def atras():
    return (f(x_0-2*h) - 4*(f(x_0-h)) + 3*(f(x_0)))/2*h


def centro():
    return (f(x_0+h) - f(x_0-h))/2*h


def adelante_5_puntos():
    return (-25*(f(x_0)) + 48*(f(x_0+h)) - 36*(f(x_0+2*h)) + 16*(f(x_0+3*h)) - 3*(f(x_0+4*h)))/12*h


def atras_5_puntos():
    return (f(x_0-2*h) - 8*(f(x_0-h)) + 8*(f(x_0+h)) - f(x_0+2*h))/12*h


def error(num_metodo):
    return round(abs((num_derivada-num_metodo)/num_derivada)*100, 3)


def impresion(num):
    er = error(num)
    print(f"numero metodo: {num} numero derivada: {num_derivada} error: {er}")


if __name__ == '__main__':
    num1 = adelante()*100    
    num2 = adelante_5_puntos()*100
    impresion(num1)
    impresion(num2)
