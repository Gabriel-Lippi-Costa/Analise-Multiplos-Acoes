def calcular_roe(lucro_liquido, patrimonio_liquido):
    roe = (lucro_liquido / patrimonio_liquido) * 100
    return round(roe, 2)