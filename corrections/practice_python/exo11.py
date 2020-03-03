def est_premier(n):
    # un nombre premier est un nombre dont les seuls diviseurs sont 1 et n.
    for d in range(2, n - 1):
        if n % d == 0:
            return False

    return True

def est_premier_joli(n):
    # all(iterable) retourne vrai si pour tout x dans iterable, x est vrai
    # any(iterable) retourne vrai s'il existe un x dans iterable tel que x est vrai.
    return all([
        n % d == 0 # est-ce que d est diviseur de n?
        for d in range(2, n - 1)
    ])

n = int(input('Donnez un joli entier: '))
print('il est premier' if est_premier(n) else 'non premier')
