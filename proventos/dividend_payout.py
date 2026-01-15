def calcular_dividend_payout(dividendos_totais, lucro_liquido):
    dividend_payout = (dividendos_totais / lucro_liquido) * 100
    return round(dividend_payout, 2)