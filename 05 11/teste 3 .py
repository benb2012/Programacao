#adicionar tarefas
#listar tarefas
#marcar tarefa como concluída
#mostrar tarefas pendentes


tarefas = []

while True:

    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Mostrar tarefas pendentes")
    print("5 - Sair")

    op = input("Escolha uma opção: ")

    # ADICIONAR
    if op == "1":

        descricao = input("Digite a descrição da tarefa: ")

        tarefa = {
            "descricao": descricao,
            "status": "pendente"
        }

        tarefas.append(tarefa)

        print("Tarefa adicionada!")

    # LISTAR
    elif op == "2":

        if len(tarefas) == 0:

            print("Nenhuma tarefa cadastrada.")

        else:

            contador = 0

            for tarefa in tarefas:

                print(contador, "-", tarefa["descricao"], "-", tarefa["status"])

                contador += 1

    # CONCLUIR
    elif op == "3":

        if len(tarefas) == 0:

            print("Nenhuma tarefa cadastrada.")

        else:

            contador = 0

            for tarefa in tarefas:

                print(contador, "-", tarefa["descricao"])

                contador += 1

            num = int(input("Digite o número da tarefa: "))

            tarefas[num]["status"] = "concluida"

            print("Tarefa concluída!")

    # PENDENTES
    elif op == "4":

        encontrou = False

        for tarefa in tarefas:

            if tarefa["status"] == "pendente":

                print("-", tarefa["descricao"])

                encontrou = True

        if encontrou == False:

            print("Não existem tarefas pendentes.")

    # SAIR
    elif op == "5":

        print("Programa encerrado.")

        break

    # INVÁLIDO
    else:

        print("Opção inválida.")