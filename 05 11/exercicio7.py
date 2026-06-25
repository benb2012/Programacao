#  Exercício 7: Lista de Presentes de Natal
# Organiza as compras natalinas, ajudando a controlar orçamento e progresso:
# Registrar presentes com nome da pessoa que vai receber, descrição do presente, valor estimado e status (comprado ou não).
# Listar todos os presentes planejados.
# Filtrar presentes já comprados e os que ainda faltam.
# Calcular o valor total planejado e o valor já gasto.
# Situação extra: permitir marcar presentes como “comprados” e atualizar automaticamente o status..






presentes = []

while True:

    print("[1]- Adicionar presente: ")
    print("[2]- Listar todos os presentes planejados: ")
    print("[3]- Filtrar presentes já comprados: ")
    print("[4]- Presentes que ainda faltam: ")
    print("[5]- Adicionar presente:")
    print("[6]- Sair: ")
    op=int(input("Escolha: "))

    if op == 1:
        destinatario = input("Nome da pessoa: ")
        descricao = input("Descrição do presente: ")
        valor = float(input("Valor estimado: "))

        presente = {
            "destinatario": destinatario,
            "descricao": descricao,
            "valor": valor,
            "comprado": False
        }

        presentes.append(presente)
        print("Presente adicionado!")

    
    elif op == 2:
        i = 0
        for p in presentes:
            if p["comprado"]:
                status = "Comprado"
            else:
                status = "Falta"

            print(i, "-", p["destinatario"], "-", p["descricao"], "-", p["valor"], "-", status)
            i += 1

  
    elif op == 3:
        for p in presentes:
            if p["comprado"]:
                print(p["destinatario"], "-", p["descricao"], "-", p["valor"])

    
    elif op == 4:
        for p in presentes:
            if not p["comprado"]:
                print(p["destinatario"], "-", p["descricao"], "-", p["valor"])

    
    elif op == 5:
        i = 0
        for p in presentes:
            print(i, "-", p["destinatario"], "-", p["descricao"])
            i += 1

        escolha = int(input("Digite o número do presente: "))

        if 0 <= escolha < len(presentes):
            presentes[escolha]["comprado"] = True
            print("Presente marcado como comprado!")
        else:
            print("Número inválido!")

    
    elif op == 6:
        total = 0
        gasto = 0

        for p in presentes:
            total += p["valor"]
            if p["comprado"]:
                gasto += p["valor"]

        print("Total planejado:", total)
        print("Total gasto:", gasto)

  
    elif op == 7:
        print("Saindo...")
        break

    else:
        print("Opção inválida!")
        

