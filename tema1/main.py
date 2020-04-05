import random
import math


def pb1():
    m = 1.0
    u = 10**(-m)

    while 1 + u != 1:
        m += 1
        u = 10**(-m)

    return u


def pb2():
    x = 5.0
    y = pb1()
    z = pb1()
    if (x * y) * z == x * (y * z):
        print('assoc', y, z)
    else:
        print('neasoc', y, z)


# '+' va fi inlocuit de '|'
# 'x' va fi inlocuit de '&'

def pb3(A, B):
    # for a in A:
    #     print(a)
    # for b in B:
    #     print(b)

    m = int(math.log(len(A), 2))  # se presupune ca logaritmul din lungimea matricii este un numar natural

    rows = int(len(A)/m) if len(A)/m == int(len(A)/m) else int(len(A)/m) + 1

    Adiv = [[[0 for k in range(0, m)] for i in range(0, len(A))] for j in range(0, rows)]
    Bdiv = [[]]

    # for i in range(0, len(Adiv)):
    #     print(Adiv[i])
    #     # for j in range(0, len(Adiv[0])):
    #     #     for k in range(0, len(Adiv[0][0])):
    #     #         print(i, j, k)
    # exit(0)

    for i in range(0, len(A)):
        #create Adiv
        for j in range(0, len(A[0])):
            Adiv[int(j / m)][i][j % m] = A[i][j]

    poz = 0
    count = 0

    for b in B:
        # create Bdiv
        if count >= m:
            count = 0
            poz += 1
            Bdiv.append([])
        Bdiv[poz].append(b)
        count += 1

    if len(Bdiv[len(Bdiv)-1]) != m:  # completam ultimul element din Bdiv cu zero-uri
        while len(Bdiv[len(Bdiv)-1]) != m:
            Bdiv[len(Bdiv)-1].append([0 for i in range(0, len(Bdiv[0][0]))])


    # for a in Bdiv:
    #     print(a)
    # for b in Bdiv:
    #     print(b)

    C = [[[0 for i in range(0, len(A))] for j in range(0, len(A))] for k in range(0, rows)]

    for i in range(0, len(Adiv)):
        for j in range(0, len(Adiv[i])):
            rws = []
            for k in range(0, len(Adiv[i][j])):
                if Adiv[i][j][k] == 1:
                    rws.append(k)

            if len(rws) > 1:
                C[i][j] = Bdiv[i][rws[0]]
                for row in rws:
                    for k in range(1, len(C[i][j])):
                        C[i][j][k] |= Bdiv[i][row][k]
            elif len(rws) == 1:
                C[i][j] = Bdiv[i][rws[0]]
            # else:
            #     fill 0, dar avem deja matricea initializata cu 0

    Cfinal = [[0 for i in range(0, len(A))] for j in range(0, len(A))]

    for i in range(0, len(C)):
        for j in range(0, len(C[i])):
            Cfinal[j] = C[i][j]
            for k in range(1, len(C[i][j])):
                Cfinal[j][k] |= C[i][j][k]

    for c in Cfinal:
        print(c)


l = 6
A = [[random.randint(0, 1) for i in range(0, l)] for j in range(0, l)]
B = [[random.randint(0, 1) for i in range(0, l)] for j in range(0, l)]


pb3(A, B)
print(pb1())
pb2()