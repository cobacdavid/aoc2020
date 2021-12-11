def main(fichier):
    with open(fichier) as fh:
        liste = list(map(int, fh.readlines()))

    i, j, k = 0, 1, 2
    while liste[i] + liste[j] + liste[k] != 2020:
        k += 1
        if k == len(liste):
            j += 1
            k = j + 1
            if j == len(liste) - 1:
                i += 1
                j = i + 1
                k = j + 1

    return liste[i] * liste[j] * liste[k]


print(main("jeu2.txt"))
