from sympy import *
import numpy as np

x = Symbol('x')
# m = [[1, 2], [0, 4], [4, -16]]
m = [[-3, 9], [5, 2], [7, -1], [8, 0]]
# m = [[0,2], [1,3], [2,2], [3,1], [4,3]]

inicio = m[0][1]
diagonal = [inicio]
columna = []
columnas = []


def clear():
    copy_col = columna.copy()
    columnas.append(copy_col)
    del columna[:]


def inicial():
    i = 0
    while i <= len(m):
        try:
            col = (m[i + 1][1] - m[i][1]) / (m[i + 1][0] - m[i][0])
            if i == 0:
                diagonal.append(int(col))
            columna.append(col)
        except Exception:
            pass
        i += 1
    clear()


def diferencias_divididas(j):
    i = 0
    while i <= len(columnas[j]):
        try:
            col = (columnas[j][i + 1] - columnas[j][i]) / (m[i + j + 2][0] - m[i][0])
            if i == 0:
                diagonal.append(col)
            columna.append(col)
        except Exception:
            pass
        i += 1
    clear()


def formula():
    x = Symbol('x')
    '''
    # 3 elementos
    print(expand(diagonal[0]+ 
        diagonal[1]*(x-m[0][0]) +
        diagonal[2]*(x-m[0][0])*(x-m[1][0])
        )
    )
    '''

    # 4 elementos
    print(expand(diagonal[0] +
                 diagonal[1] * (x - m[0][0]) +
                 diagonal[2] * (x - m[0][0]) * (x - m[1][0]) +
                 diagonal[3] * (x - m[0][0]) * (x - m[1][0]) * (x - m[2][0])
                 )
          )

    '''
    # 5 elementos
    print(expand(diagonal[0]+ 
        diagonal[1]*(x-m[0][0]) +
        diagonal[2]*(x-m[0][0])*(x-m[1][0]) +
        diagonal[3]*(x-m[0][0])*(x-m[1][0])*(x-m[2][0]) +
        diagonal[4]*(x-m[0][0])*(x-m[1][0])*(x-m[2][0])*(x-m[3][0])
       )
    )
    '''


def print_matrix():
    matrix = np.zeros((len(m), len(m) + 2))
    # Always
    for i in range(len(m)):
        matrix[i][0] = i
    for i in range(len(m)):
        matrix[i][1] = m[i][0]
    for i in range(len(m)):
        matrix[i][2] = m[i][1]
    # Column 3
    for i in range(len(columnas[0])):
        matrix[i + 1][3] = columnas[0][i]
    # Column 4
    for i in range(len(columnas[1])):
        matrix[i + 2][4] = columnas[1][i]
    # Column 5
    for i in range(len(columnas[2])):
        matrix[i + 3][5] = columnas[2][i]
    '''
    # Column 6
    for i in range(len(columnas[3])):
        matrix[i+4][6] = columnas[3][i]
    '''
    print(matrix)


if __name__ == '__main__':
    inicial()
    j = 0
    while True:
        if len(columnas[j]) != 1:
            diferencias_divididas(j)
            j += 1
        else:
            break
    print(diagonal)
    print(columnas)
    formula()
    print_matrix()
