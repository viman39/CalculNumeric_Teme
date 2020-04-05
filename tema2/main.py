import numpy as np


def determinant(matrix):
    return np.linalg.det(np.array(matrix))


def doolittle(mat):
    n = len(mat)

    L = [[0 for x in range(n)] for y in range(n)]
    U = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(i, n):
            s = 0
            
            for k in range(i):
                s += (L[i][k] * U[k][j])

            U[i][j] = mat[i][j] - s

        for j in range(i, n):
            if i == j:
                L[i][i] = 1
            else:
                s = 0
                for k in range(i):
                    s += (L[j][k] * U[k][i])

                L[j][i] = (mat[j][i] - s) / U[i][i]

    return U, L


def detA(A):
    U, L = doolittle(A)

    return determinant(U) * determinant(L)


def bulina3(A, B):
    n = len(A)

    Y = [[0] for i in range(0, n)]

    for i in range(0, n):
        s = 0

        for j in range(0, i):
            s += ((1 if i == j else A[i][j]) * Y[j][0])

        Y[i][0] = (B[i][0] - s)

    X = [[0] for i in range(0, n)]

    for i in range(n-1, -1, -1):
        s = 0

        for j in range(i+1, n):
            s += (A[i][j] * X[j][0])

        X[i][0] = (Y[i][0] - s) / A[i][i]

    return X


def bulina4(ainit, binit):
    ainit = np.array(ainit)
    binit = np.array(binit)
    ainitxlu = np.subtract(ainit.dot(bulinaX(ainit, binit)), binit)

    return np.linalg.norm(ainitxlu)


def bulina5(L, U):
    single = [[0 for i in range(0, len(L))] for i in range(0, len(L))]

    for i in range(0, len(U)):
        for j in range(0, len(U)):
            if i > j:
                single[i][j] = L[i][j]
            else:
                single[i][j] = U[i][j]

    return single


def bulinaX(ainit, binit):
    Anp = np.array(ainit)
    Anp = np.linalg.inv(Anp)
    bnp = np.array(binit)

    return Anp.dot(bnp)


def bulina6(ainit, binit, xLU, xLIB):
    ainitnp = np.array(ainit)
    binitnp = np.array(binit)
    xLUnp = np.array(xLU)
    xLIBnp = np.array(xLIB)
    am1 = np.linalg.inv(ainitnp)
    print("matrix X:\n", np.array(bulinaX(ainit, binit)))
    print("invers: \n", am1)
    print("norma xLU - xLIB: ", np.linalg.norm(np.subtract(xLUnp, xLIBnp)))
    print("norma xLU - A-1 * binit: ", np.linalg.norm(np.subtract(xLUnp, am1.dot(binitnp))))


mat = [[2.5, 2, 2],
       [5, 6, 5],
       [5, 6, 6.5]]

binit = [[2], [2], [2]]

U, L = doolittle(mat)
print("\nbulina1")
print("doolittle upper:\n", np.array(U))
print("doolittle lower:\n", np.array(L))

print("\nbulina2")
print("det(A): ", determinant(mat))
print("det(L) * det(U): ", detA(mat))

print("\nbulina5")
single = bulina5(L, U)
print("single array:\n", np.array(single))

print("\nbulina3")
X = bulina3(single, binit)
print("matrix X: \n", np.array(X))

print("\nbulina4")
print("norma: ", bulina4(mat, binit))

print("\nbulina6")
bulina6(mat, binit, X, bulinaX(mat, binit))
