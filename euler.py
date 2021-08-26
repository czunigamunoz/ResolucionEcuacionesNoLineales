def f(x, y): 
    return y-x**2+1

# Condicion inicial
x_0 = 0
y_0 = 1
h = 0.1
n = 6

def x(x):
    return x + h
def y(x, y):
    return y + h*(f(x, y))

def metodo_euler():
    global x_0, y_0
    for i in range(n+1):
        print(f"X{i} = {x_0}   Y{i} = {y_0}")
        x_temp = x_0
        x_0 = round(x(x_0), 2)
        y_0 = round(y(x_temp, y_0), 7)

metodo_euler()