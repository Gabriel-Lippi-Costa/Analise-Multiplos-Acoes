def calcular_indice_cobertura_dividendos_caixa_conservadora(fluxo_caixa_livre, dividendos_pagos):
    cdc_conservador = fluxo_caixa_livre / dividendos_pagos
    return round(cdc_conservador, 2)