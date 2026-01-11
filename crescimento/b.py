def calcular_b_proporcao_lucro_reinvestido(lucro_liquido, dividendos):
    b = (lucro_liquido - dividendos) / lucro_liquido
    return round(b, 4)