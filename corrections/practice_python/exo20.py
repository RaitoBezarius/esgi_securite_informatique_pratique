def chercher(L, x):
    for y in L:
        if x == y:
            return True

    return False


def dichotomie(L, x):
    if not L: # cas de la liste vide
        return False

    if len(L) == 1:
        return L[0] == x #  cas de la liste à un élément

    middle = len(L)//2

    if L[middle] == x:
        return True
    elif L[middle] < x:
        return dichotomie(L[middle:], x)
    else:
        return dichotomie(L[:middle], x)
