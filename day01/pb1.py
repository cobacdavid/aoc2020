def main(fichier):
    with open(fichier) as fh:
        liste = list(map(int, fh.readlines()))

    i, j = 0, 1
    while liste[i] + liste[j] != 2020:
        j += 1
        if j == len(liste):
            j = 1
            i += 1
    return liste[i] * liste[j]


print(main("jeu2.txt"))
