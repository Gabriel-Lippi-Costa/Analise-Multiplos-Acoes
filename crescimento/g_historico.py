def calcular_g_historico(lpa_atual, lpa_anterior):
    crescimento = ((lpa_atual / lpa_anterior) - 1) * 100
    return round(crescimento, 2) 