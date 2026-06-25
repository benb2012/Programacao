#O programa precisa:

#registrar despesas
#listar despesas
#filtrar por categoria
#calcular total gasto

despesas = []

while True:

    print("\n1 - Registrar despesa")
    print("2 - Listar despesas")
    print("3 - Filtrar por categoria")
    print("4 - Calcular total gasto")
    print("5 - Sair")

    op = input("Escolha: ")

    # REGISTRAR
    if op == "1":

        data = input("Data: ")

        valor = float(input("Valor: "))

        categoria = input("Categoria: ")

        descricao = input("Descrição: ")

        despesa = {
            "data": data,
            "valor": valor,
            "categoria": categoria,
            "descricao": descricao
        }

        despesas.append(despesa)

        print("Despesa registrada!")

    # LISTAR
    elif op == "2":

        if len(despesas) == 0:

            print("Nenhuma despesa registrada.")

        else:

            contador = 0

            for despesa in despesas:

                print("\nDespesa", contador)

                print("Data:", despesa["data"])

                print("Valor:", despesa["valor"])

                print("Categoria:", despesa["categoria"])

                print("Descrição:", despesa["descricao"])

                contador += 1

    # FILTRAR
    elif op == "3":

        categoria_busca = input("Digite a categoria: ")

        encontrou = False

        for despesa in despesas:

            if despesa["categoria"] == categoria_busca:

                print(despesa["descricao"], "-", despesa["valor"])

                encontrou = True

        if encontrou == False:

            print("Categoria não encontrada.")

    # TOTAL
    elif op == "4":

        total = 0

        for despesa in despesas:

            total = total + despesa["valor"]

        print("Total gasto:", total)

    # SAIR
    elif op == "5":

        print("Programa encerrado.")

        break

    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida.")