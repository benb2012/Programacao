tarefas = []

while True:

    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Mostrar tarefas pendentes")
    print("5 - Sair")

    op = input("Escolha uma opção: ")

    # ADICIONAR TAREFA
    if op == "1":

        descricao = input("Digite a descrição da tarefa: ")

        tarefa = {
            "descricao": descricao,
            "status": "pendente"
        }

        tarefas.append(tarefa)

        print("Tarefa adicionada com sucesso!")

    # LISTAR TODAS
    elif op == "2":

        if len(tarefas) == 0:

            print("Nenhuma tarefa cadastrada.")

        else:

            for i, tarefa in enumerate(tarefas):

                print(i, "-", tarefa["descricao"], "-", tarefa["status"])

    # MARCAR COMO CONCLUÍDA
    elif op == "3":

        if len(tarefas) == 0:

            print("Nenhuma tarefa cadastrada.")

        else:

            for i, tarefa in enumerate(tarefas):

                print(i, "-", tarefa["descricao"], "-", tarefa["status"])

            num = int(input("Digite o número da tarefa: "))

            tarefas[num]["status"] = "concluida"

            print("Tarefa concluída!")

    # MOSTRAR PENDENTES
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

    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida.")