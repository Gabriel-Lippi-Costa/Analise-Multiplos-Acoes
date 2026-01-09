def calcular_g_projetivo(roe, payout):
    g_projetivo = roe * (1 - payout)
    return round(g_projetivo * 100, 2)