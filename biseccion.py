import sympy as sy
import pprint

x = sy.Symbol('x')
a_i, b_i = 17, 22.2
n = 14


def f(x_var):
    return x_var ** 5 - 100 * x_var ** 4 + 3995 * x_var ** 3 - 79700 * x_var ** 2 + 794004 * x_var - 3160075


def fun_continua(num):
    resp1 = sy.limit(f(x), x, num)
    resp2 = f(num)
    return True if resp1 == resp2 else False


def fun_signos_opuestos(num1, num2):
    return True if ((num1 > 0 and num2 < 0) or (num1 < 0 and num2 > 0)) else False


continua = fun_continua(a_i) and fun_continua(b_i)
signos = fun_signos_opuestos(f(a_i), f(b_i))

if continua and signos:
    i = 1
    while True:
        f_a = f(a_i)
        f_b = f(b_i)
        p_i = (a_i + b_i) / 2
        f_p = f(p_i)
        pprint.pprint(f"{i} a_i: {round(a_i, n)} b_i: {round(b_i, n)} p_i: {round(p_i, n)} f_p: {f_p}", width=150)
        a_i = p_i if fun_signos_opuestos(f_a, f_p) is False else a_i
        b_i = p_i if fun_signos_opuestos(f_b, f_p) is False else b_i
        i += 1
        if f_p == 0:
            print(f"Interaccion: {i - 1} -- Raiz: {p_i}")
            break
