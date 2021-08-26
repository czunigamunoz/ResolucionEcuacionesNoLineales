f = lambda x, y: 2 * x * y

# Condicion inicial
x_0 = 0
y_0 = 1
h = 0.1
n = 10
num_redondeo = 7

x = lambda x: x + h
y = lambda y, k1, k2, k3, k4: y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def metodo_runge_kutta():
    global x_0, y_0
    for i in range(n + 1):
        k1 = f(x_0, y_0)
        k2 = f(x_0 + (h / 2), y_0 + (h / 2) * k1)
        k3 = f(x_0 + (h / 2), y_0 + (h / 2) * k2)
        k4 = f(x_0 + h, y_0 + h * k3)
        print(
            f"X{i} = {round(x_0, num_redondeo)} Y{i} = {round(y_0, num_redondeo)}"
            f" \t k1= {round(k1, num_redondeo)} k2 = {round(k2, num_redondeo)} k3 = {round(k3, num_redondeo)} k4 = {round(k4, num_redondeo)}",
            end='\n\n')
        y_0 = y(y_0, k1, k2, k3, k4)
        x_0 = x(x_0)


metodo_runge_kutta()
