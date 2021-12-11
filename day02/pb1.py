def main(fichier):
    with open(fichier) as fh:
        somme = 0
        for ligne in fh:
            policy, password = ligne.strip().split(':')
            contrainte, car = policy.split()
            lemin, lemax = list(map(int, contrainte.split("-")))
            somme += lemin <= password.count(car) <= lemax
    return somme


print(main("jeu2.txt"))
