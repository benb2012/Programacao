from apuracao import *

for i in range(10):
    computar_voto(apuracao)

print("\n--- RESULTADO ---")

print("Vencedor:", obter_vencedor(apuracao))

print("\nRelatório:")
relatorio = gerar_relatorio(apuracao)

for item in relatorio:
    print(item[0], "-", f"{item[1]:.2f}%")