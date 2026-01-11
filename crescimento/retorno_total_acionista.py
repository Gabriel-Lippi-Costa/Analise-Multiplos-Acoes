def calcular_retorno_total_acionista(dividendos, valor_final_acao, valor_inicial_acao):
    rta = ((valor_final_acao - valor_inicial_acao) + dividendos) / valor_inicial_acao * 100
    return rta