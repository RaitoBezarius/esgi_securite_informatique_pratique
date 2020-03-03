from collections import Counter

def supprimerDoublonsLent(L):
    L_dedoublonne = []

    # On itère sur les éléments de L.
    for x in L:
        # Avons-nous vu x dans la liste dédoublonnée? Si non, on l'ajoute!
        if x not in L_dedoublonne: # Ceci nécessite de parcourir la liste entièrement, c'est lent !
            # On l'ajoute à la fin.
            L_dedoublonne.append(x)

    return L_dedoublonne

def supprimerDoublonsUnPeuMieux(L):
    L.sort() # On trie L dans l'ordre croissant – O(len(L) log len(L)) en complexité temporelle.
    L_dedupe = []

    # On itère sur les couples (indice, valeur), i.e. L[indice] == valeur!
    for i, x in enumerate(L):
        # On s'en fiche du premier élément, il est toujours unique.
        if i == 0:
            L_dedupe.append(x)
            continue

        # À présent, i ≥ 1 donc i - 1 ≥ 0!
        # Ignorons les doublons (puisqu'ils sont dans l'ordre!)
        if L_dedupe[i - 1] == L_dedupe[i]:
            continue

        # À ce stade-là, on sait qu'on est pas un doublon nécessairement.
        L_dedupe.append(x)

    return L_dedupe

def supprimerDoublonsParfait(L):
    return list(set(L))

def supprimerDoublonsBonus(L):
    occurrences = Counter(L)
    # TODO: implémentez le reste!
