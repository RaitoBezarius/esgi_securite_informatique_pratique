def executer_intcode(prg):
    i = 0
    while i < len(prg):
        # syntaxe de slicing!
        opcode, p1, p2, out = L[i:i + 4]

        if opcode not in (1, 2, 99):
            raise ValueError("Opcode invalide détecté, exécution impossible ou programme corrompu!")

        if opcode == 1:
            prg[out] = prg[p1] + prg[p2]
        elif opcode == 2:
            prg[out] = prg[p1] * prg[p2]
        else: # on sait que opcode == 99 d'après la ligne 7.
            break
    return prg[0]
