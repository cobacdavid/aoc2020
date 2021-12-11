def main(fichier):
    with open(fichier) as fh:
        pos = 0
        n = len(fh.readline().strip())
        inc = 3
        arbres = 0
        for ligne in fh:
            pos = (pos + inc) % n
            arbres += ligne[pos] == "#"
    return arbres


print(main("jeu2.txt"))
