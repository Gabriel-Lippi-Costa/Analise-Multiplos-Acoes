def calcular_earning_yield(lucro_por_acao, preco_atual):
    earning_yield = (lucro_por_acao / preco_atual) * 100
    return round(earning_yield, 2)