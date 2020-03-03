def diviseurs(n):
    # 1 est toujours diviseur de n, oui, en effet: n = n * 1…
    diviseurs = [1]
    # on parcourt de 2 à n.
    # N.B: on peut parcourir de 2 à n - 1 et ajouter n à la fin, puisque n divise toujours n.
    for d in range(2, n + 1):
        if n % d == 0: # n modulo d = 0 si et seulement si n = d*q pour un certain q, i.e. d divise n!
            diviseurs.append(d)
    return diviseurs

# version compréhension de liste
def diviseurs_oneliner(n):
    return [d for d in range(1, n + 1) if n % d == 0]

n = int(input('Entrez un entier: '))
print(diviseurs(n))
