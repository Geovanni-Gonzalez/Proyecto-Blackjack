def monteCarlo(mazo, mano):
    simulaciones = 1000
    hitsAcertados = 0
    for _ in range(simulaciones):
        simulacionMano = mano[:]
        simulacionMazo = mazo[:]
        carta = simulacionMazo.pop()
        simulacionMano.append(carta)
        if valorMano(simulacionMano) <= 21:
            hitsAcertados += 1
    return hitsAcertados / simulaciones


def valorMano(mano):
    valor = 0
    ases = 0
    for carta in mano:
        if carta.getValorNumerico() == 1:
            ases += 1
        valor += carta.getValorNumerico()
    while valor < 12 and ases > 0:
        valor += 10
        ases -= 1
    return valor