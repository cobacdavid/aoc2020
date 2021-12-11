def main(fichier):
    with open(fichier) as fh:
        somme = 0
        for ligne in fh:
            policy, password = ligne.strip().split(':')
            password = password.lstrip()
            contrainte, car = policy.split()
            pos1, pos2 = list(map(int, contrainte.split("-")))
            b1 = password[pos1 - 1] == car
            b2 = password[pos2 - 1] == car
            somme += b1 != b2
    return somme


print(main("jeu2.txt"))
