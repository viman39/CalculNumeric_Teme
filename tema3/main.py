def generate_matrix(file):
    f = open(file, "r")
    lines = f.read().split('\n')

    n = int(lines[0])

    # initializam o matrice cu len(a) dictionare,
    # mat[n] reprezinta elementele de pe linia n din matrice
    # key-le dictionarului reprezinta coloana si valoare din key reprezinta valoarea din matrice
    # practic mat[n][key] reprezinta valoarea din matrice de la linia n si coloana key
    mat = [{} for i in range(0, n)]

    # zeros numara zerourile pentru linie din matrice
    zeros = [0 for i in range(0, n)]

    for line in lines[1:]:
        # pentru fiecare linie din fisier verificam sa nu fie linia un empty string
        if line.strip() == "":
            continue

        # facem split() dupa "," si obtinem un array cu 3 valori
        info = line.split(",")

        linie_mat = int(info[1])
        val_mat = float(info[0])
        col_mat = int(info[2])

        mat[linie_mat][col_mat] = val_mat
        zeros[linie_mat] += 1

        if zeros[linie_mat] > 11 and file not in ["aorib.txt", "aplusb.txt"]:
            # verificam ca in cazul in care citim matricele de baza ( a si b ) sa nu avem mai mult de 10 elemente nenule pe o linie
            print("Eroare! Linia " + info[1] + " are mai mult de 10 elemente nenule")
            return

    # ordonam dictionarele dupa cheie
    for i in range(0, len(mat)):
        mat[i] = dict(sorted(mat[i].items()))

    return mat


def aplusb(a, b):
    # initializam suma cu matricea a
    suma = a

    # pentru fiecare element din b, daca gasim (linia,key-ul) in matricea suma
    # adaugam valoare din b[linie][key] la suma[linie][key]
    # altfel cream key-ul key pentru linia linie din b
    for i in range(0, len(b)):
        for key in b[i].keys():
            if key in suma[i].keys():
                suma[i][key] += b[i][key]
            else:
                suma[i][key] = b[i][key]

    # ordonam dictionarul de la final
    for i in range(0, len(suma)):
        suma[i] = dict(sorted(suma[i].items()))

    return suma


def aorib(a, b):
    # initializam matricea produs (rezultatul inmultirii) cu len(a) dictionare
    produs = [{} for i in range(0, len(a))]

    # pentru fiecare element din matricea "mare" (adica toate elementele de la 0, len(a) pe linie si pe coloana)
    # calculam rezultatul
    # care o sa fie suma ( a[linie][coloana] * b[coloana][linie] )
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            rez = 0

            # pentru toate key-urile de pe linia a[i]
            # daca gasim indexul coloanei in key-urile b[key]
            # adunam la rezultat a[linie][key] * b[key][coloana]
            for key in a[i].keys():
                if j in b[key].keys():
                    rez += a[i][key] * b[key][j]

            # daca rezultatul e diferit de 0 il adaugam pe linia corespunzatoare
            if rez != 0:
                produs[i][j] = rez

    # ordonam dictionarele din matrice
    for i in range(0, len(produs)):
        produs[i] = dict(sorted(produs[i].items()))

    return produs


# generam matricea rara din fiserul txt
a_rara = generate_matrix("a.txt")
b_rara = generate_matrix("b.txt")
[print(a) for a in b_rara]
print("Matricea b_rara")
check = True

# generam matricea aorib din fisier
aob = generate_matrix("aorib.txt")
aobmeu = aorib(a_rara, b_rara)

# verificam dictionarele de pe fiecare linie din matricea calculata de mine si matricea din fisier
# daca gasim 2 linii diferite specificam matricea in care apare inegalitatea si cele 2 linii din matrice
for i in range(0, len(aobmeu)):  # verificare a ori b
    if aobmeu[i] != aob[i]:
        print("inmultire")
        print(aobmeu[i])
        print(aob[i])
        print()
        check = False

# daca nu am gasit nici un dictinoar care sa nu fie identic cu corespondentul lui din fisier
# afisam un mesaj
if check == False:
    print("inmultirea nu e buna :(")
else:
    print("inmultirea e buna :)")


check = True

apb = generate_matrix("aplusb.txt")
apbmeu = aplusb(a_rara, b_rara)

for i in range(0, len(apbmeu)):  # verificare a plus b al meu sa fie la fel ca cel din fisier
    if apbmeu[i] != apb[i]:
        print("adunare")
        print(apbmeu[i])
        print(apb[i])
        print()
        check = False


if check == False:
    print("adunarea nu e buna :(")
else:
    print("adunarea e buna :)")
