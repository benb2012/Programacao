vagas = 10
total_carros = 0

while True:
    comando = input("Deseja estacionar? (Digite 'fechar' para sair): ")

    if comando == "fechar":
        break

    if vagas > 0:
        vagas = vagas - 1
        total_carros = total_carros + 1
        print(f"Vagas restantes: {vagas}")
    else:
        print("Estacionamento lotado")

print(f"Total de carros atendidos: {total_carros}")