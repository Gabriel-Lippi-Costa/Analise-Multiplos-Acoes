def calcular_indice_liquidez_corrente(ativo_circulante, passivo_circulante):
    indice_liquidez_corrente = ativo_circulante / passivo_circulante
    return round(indice_liquidez_corrente, 2)