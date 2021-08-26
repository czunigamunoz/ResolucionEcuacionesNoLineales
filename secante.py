import numpy as np
from scipy import optimize

f = lambda x: np.exp(-x) + x - 2
a = 0
b = 1

raiz = optimize.root_scalar(f, x0=a, x1=b, method='secant')
print(raiz)
