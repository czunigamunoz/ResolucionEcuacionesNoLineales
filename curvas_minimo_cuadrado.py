x_i = [7.2, 6.7, 17.0, 12.5, 6.3, 23.9, 6.0, 10.2]
y_i = [4.2, 4.9, 7.0, 6.2, 3.8, 7.6, 4.4, 5.4]
n = len(x_i)


def sum_xi_yi():
    result = 0
    for x, y in zip(x_i, y_i):
        result += x * y
    return result


def sum_xi_cuadrado():
    result = 0
    for x in x_i:
        result += x ** 2
    return result


def sum_xi():
    result = 0
    for x in x_i:
        result += x
    return result


def sum_yi():
    result = 0
    for y in y_i:
        result += y
    return result


def a():
    return ((n * (sum_xi_yi())) - (sum_xi()) * (sum_yi())) / (n * (sum_xi_cuadrado()) - (sum_xi()) ** 2)


def b():
    return ((sum_yi()) * (sum_xi_cuadrado()) - (sum_xi()) * (sum_xi_yi())) / (n * (sum_xi_cuadrado()) - (sum_xi()) ** 2)


print(f"Y = {a()}x + {b()}")
