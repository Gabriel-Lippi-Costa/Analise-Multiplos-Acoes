def calcular_indice_cobertura_dividendos_caixa_basica(fluxo_caixa_operacional, dividendos_pagos):
    cdc_basico = fluxo_caixa_operacional / dividendos_pagos
    return round(cdc_basico, 2)