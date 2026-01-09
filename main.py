import rentabilidade.margem_liquida
import rentabilidade.roe
import valuation.preco_lucro
import crescimento.g_historico
import crescimento.g_projetivo
import valuation.preco_lucro_crescimento_historico
import valuation.preco_lucro_crescimento_projetivo
import valuation.earning_yields  


print("Seção de Crescimento")
print(f"g Histórico: {crescimento.g_historico.calcular_g_historico(120000, 100000)}%")
print(f"g Projetivo: {crescimento.g_projetivo.calcular_g_projetivo(0.15, 0.4)}%")
print("")
print("--------------------------------")

print("Seção de Proventos")
print("")
print("--------------------------------")

print("Seção de Rentabilidade")
print(f"Margem líquida: {rentabilidade.margem_liquida.calcular_margem_liquida(50000, 500000)}%")
print(f"ROE: {rentabilidade.roe.calcular_roe(150000, 1000000)}%")
print("")
print("--------------------------------")

print("Seção de Solvência")
print("")
print("--------------------------------")

print("Seção de Valuation")
print(f"P/L: {valuation.preco_lucro.calcular_preco_lucro(50, 5)}")
print(f"PEG Histórico: {valuation.preco_lucro_crescimento_historico.calcular_preco_lucro_crecimento_historico(15, 50)}")
print(f"PEG Projetivo: {valuation.preco_lucro_crescimento_projetivo.calcular_preco_lucro_crecimento_projetivo(15, 12)}")
print(f"Earning Yield: {valuation.earning_yields.calcular_earning_yield(4.50, 29.99)}%")
print("")
print("--------------------------------")
