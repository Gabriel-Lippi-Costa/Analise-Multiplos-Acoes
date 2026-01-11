#Esse algoritmo calcula o dividend yield dos últimos doze meses para uma ação específica.

def calcular_dividend_yield_doze_meses(dividendos_ano_passado, preco_acao):
    dividend_yield_doze_meses = (dividendos_ano_passado / preco_acao) * 100
    return round(dividend_yield_doze_meses, 2)