def main(fichier):
    with open(fichier) as fh:
        pos = 0
        n = len(fh.readline().strip())
        inc = [1, 3, 5, 7, 1]
        arbres = [0] * 5
        pos = [0] * 5
        for k, ligne in enumerate(fh):
            for i in range(4):
                pos[i] = (pos[i] + inc[i]) % n
                arbres[i] += ligne[pos[i]] == "#"
            if k % 2 == 1:
                pos[4] = (pos[4] + inc[4]) % n
                arbres[4] += ligne[pos[4]] == "#"

    p = 1
    for a in arbres:
        p *= a
    return p


print(main("jeu2.txt"))
