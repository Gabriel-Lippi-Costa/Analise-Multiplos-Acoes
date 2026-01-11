import crescimento.g_historico
import crescimento.g_projetivo
import crescimento.b
import crescimento.retorno_total_acionista

import proventos.dividend_yield_doze_meses
import proventos.dividend_yield_on_cost
import proventos.dividend_yield_seis_anos

import rentabilidade.margem_liquida
import rentabilidade.roe

import solvencia.fluxo_caixa_livre
import solvencia.indice_liquidez_corrente

import valuation.preco_lucro_crescimento_historico
import valuation.preco_lucro_crescimento_projetivo
import valuation.preco_lucro
import valuation.earning_yields  


print("Seção de Crescimento")
print(f"g Histórico: {crescimento.g_historico.calcular_g_historico(120000, 100000)}%")
print(f"g Projetivo: {crescimento.g_projetivo.calcular_g_projetivo(0.15, 0.4)}%")
print(f"b: {crescimento.b.calcular_b_proporcao_lucro_reinvestido(100, 25)}%")
print(f"Retorno Total ao Acionista: {crescimento.retorno_total_acionista.calcular_retorno_total_acionista(4, 46, 40)}%")
print("")
print("--------------------------------")

print("Seção de Proventos")
print(f"Dividend Yield (12 meses): {proventos.dividend_yield_doze_meses.calcular_dividend_yield_doze_meses(1.8, 30)}%")
print(f"Dividend Yield on Cost: {proventos.dividend_yield_on_cost.calcular_dividend_yield_on_cost(1.80, 20)}%")
print(f"Dividend Yield (6 anos): {proventos.dividend_yield_seis_anos.calcular_dividend_yield_seis_anos(2.45, 40)}%")
print("")
print("--------------------------------")

print("Seção de Rentabilidade")
print(f"Margem líquida: {rentabilidade.margem_liquida.calcular_margem_liquida(50000, 500000)}%")
print(f"ROE: {rentabilidade.roe.calcular_roe(150000, 1000000)}%")
print("")
print("--------------------------------")

print("Seção de Solvência")
print(f"Fluxo de Caixa Livre: R${solvencia.fluxo_caixa_livre.calcular_fluxo_caixa_livre(500000 , 150000)}")
print(f"Índice de Liquidez Corrente: {solvencia.indice_liquidez_corrente.calcular_indice_liquidez_corrente(150000, 100000)}")
print("")
print("--------------------------------")

print("Seção de Valuation")
print(f"P/L: {valuation.preco_lucro.calcular_preco_lucro(50, 5)}")
print(f"PEG Histórico: {valuation.preco_lucro_crescimento_historico.calcular_preco_lucro_crecimento_historico(15, 50)}")
print(f"PEG Projetivo: {valuation.preco_lucro_crescimento_projetivo.calcular_preco_lucro_crecimento_projetivo(15, 12)}")
print(f"Earning Yield: {valuation.earning_yields.calcular_earning_yield(4.50, 29.99)}%")
print("")
print("--------------------------------")
