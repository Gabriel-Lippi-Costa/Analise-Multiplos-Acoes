#Esse algoritmo calcula o dividend yield dos últimos seis anos para uma ação específica, o ano atual não entra em consideração.

def calcular_dividend_yield_seis_anos(dpa_medio, preco_atual_acao):
    dividend_yield_seis_anos = (dpa_medio / preco_atual_acao) * 100
    return round(dividend_yield_seis_anos, 2)