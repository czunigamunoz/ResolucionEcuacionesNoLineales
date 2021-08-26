from scipy import optimize


def f(x):
    return x ** 5 - 100 * x ** 4 + 3995 * x ** 3 - 79700 * x ** 2 + 794004 * x - 3160075


a = 17
b = 22.2
tolerance = 1 * 10 ** -14

raiz = optimize.root_scalar(f, bracket=[a, b], xtol=tolerance, method='bisect')
print(raiz)
