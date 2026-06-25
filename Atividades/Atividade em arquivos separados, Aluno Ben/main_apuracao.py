from apuracao import * 

while True:
    print("\n=== MENU DE VOTAÇÃO ===")
    print("1. Votar")
    print("2. Ver Vencedor Atual")
    print("3. Ver Relatório Completo")
    print("4. Sair do Programa")
    
    opcao = input("Escolha uma opção (1-4): ")
    print() 

    if opcao == "1":
        computar_voto(apuracao)
        
    elif opcao == "2":
        ganhador = obter_vencedor(apuracao)
        print("Vencedor atual:", ganhador)
        
    elif opcao == "3":
        print("--- Relatório de Votos ---")
        lista_relatorio = gerar_relatorio(apuracao)
        
        for item in lista_relatorio:
       
            print(item[0], "-", f"{item[1]:.2f}%")
            
    elif opcao == "4":
        print("Encerrando o sistema. Até logo!")
        break
        
    else:
        print("Opção inválida! Tente novamente.")