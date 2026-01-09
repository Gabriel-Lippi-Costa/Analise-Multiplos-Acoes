import rentabilidade.margem_liquida
import rentabilidade.roe
import valuation.preco_lucro
import crescimento.g_historico
import crescimento.g_projetivo


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
print("")
print("--------------------------------")
