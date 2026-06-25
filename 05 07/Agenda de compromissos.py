lista = []

#adicionar os compromissos
while (True):
    print("\n---Menu---")
    print("1 - Adicionar compromisso")
    print("2 - listar compromissos ")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção"))

    if (opcao == 1):
        data = input ("Digite a data (dd/mm/yyyy) ")
        hora = input ("Digite a hora (hh:mm)" )
        descricao = input ("digite a descriçao" )
        local = input ("Digite o local: ")

        compromisso = {
            "data": data,
            "hora": hora,
            "descricao": descricao,
            "local": local
        }

        lista.append(compromisso)
        print("Compromisso adicionado com sucesso!")
    elif opcao == 2:
        if len(lista)==0:
            print("Nenhum compromisso resgistrado.")
        else:
            for item in lista:
                print (item['data'], item['hora'],
                       item['descriçao'], item ['local'])
    elif opcao == 3:
        print("ENCERRANDO O PROGRAMA...")
        break
    else:
        print("Opção invalida, tente novamente.")