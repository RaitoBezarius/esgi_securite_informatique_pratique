def max_de_trois(a, b, c):
    # chaînes d'inégalités
    # on a 6 cas possibles (les permutations à trois éléments: factorielle de 3 = 3 × 2 × 1 = 6).
    if a <= b <= c:
        return c
    elif a <= c <= b:
        return b
    elif c <= b <= a:
        return a
    elif b <= c <= a:
        return a
    elif c <= a <= b:
        return b
    elif b <= a <= c:
        return c
    else:
        raise RuntimeError('Cas impossible!')

def max_flemmard(a, b, c):
    return max(a, max(b, c))

def max_flemmard2(a, b, c):
    return max([a, b, c])

# Uns de vos camarades a tenté de généraliser l'exercice à une quantité infini d'arguments.
# Lorsque vous mettez *parametre, tous les arguments sont absorbés dans une liste parametre.
def max_generalise(*elements):
    # elements[0] est le premier argument, elements[1] le second, etc.

    # si la liste est vide
    if not elements:
        raise RuntimeError('Je ne connais pas trop le max de la liste vide…')

    max_ = elements[0]

    # notation slicing: tableau[start:end:step] retourne le tableau formé par les valeurs aux indices start + k*step pour 0 ≤ k ≤ (end - start)/step
    # autrement dit, si t = [1, 2, 3, 4]
    # vous regardez t[1:2], ça fait [2, 3], testez cette syntaxe!
    for x in elements[1:]: # on itère qu'à partir de 2nde valeur, puisque on a déjà regardé la première valeur.
        max_ = max_ if max_ >= x else x # syntaxe ternaire: (expression if condition else expression_dans_le_cas_faux)

    return max_
