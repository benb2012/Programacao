#  Exercício 6 - Venda de Ingressos para Show
# Simula um sistema de bilheteria, incluindo controle de estoque e cálculo de receita.:
# Registrar ingressos vendidos com nome do comprador, tipo de ingresso (pista, camarote, VIP), valor e forma de pagamento.
# Listar todos os ingressos vendidos.
# Filtrar ingressos por tipo (ex: apenas VIP).
# Calcular o total arrecadado.
# # Situação extra: limitar a quantidade de ingressos disponíveis por categoria (ex: 100 pista, 50 camarote, 20 VIP). Se esgotar, não permitir novas vendas.
tipos= [
{"tipo":"pista", "valor": 50, "quantidade": 100},
{"tipo":"camarote", "valor": 100, "quantidade": 50},
{"tipo":"VIP", "valor": 150, "quantidade": 20}
]

ingressos = []
receita = 0 
while True:
    print(f"[1]- Registar ingresso")
    print(f"[2]- Listar ingressos vendidos")
    print(f"[3]- Filtrar ingressos por tipo")
    print(f"[4]- Calcular total arrecadado")
    print(f"[5]- Verificar quantidade")
    print(f"[6]- SAIR")

    op = int(input("Escolha: "))

    if op == 1:
        nome= input("Digite seu nome para regitro: ")

        tipo = input("Selecione o tipo de ingresso\n [1] pista\n [2] camarote\n [3] VIP\n")
        if tipo==1:
            if tipos[0]["quantidade"]>0:
                nome_tipo = "pista"
                tipos[0]["quantidade"]-=1
                valor = tipos[0]["quantidade"]
            else:
                print("Não há ingressos")
        if tipo==2:
            if tipos[1]["quantidade"]>0:
                nome_tipo = "camarote"
                tipos[1]["quantidade"]-=1
                valor = tipos[1]["quantidade"]
            else:
                print("Não há ingressos")
        if tipo==3:
            if tipos[2]["quantidade"]>0:
                nome_tipo = "VIP"
                tipos[2]["quantidade"]-=1
                valor = tipos[2]["quantidade"]
            else:
                print("Não há ingressos")
        formadp= input(f"O valor é {valor},Qual a forma de pagamento?: ")
    
        ingresso = {
            "tipo":tipo,
            "nome":nome,
            "valor":valor,
            "forma de pagamento":formadp
        }
        ingressos.append(ingresso)
        receita += valor
    if op == 2:
        for p in ingressos:
            print(f"Comprador- {p["nome"]},\t tipo- {p["tipo"]},\t valor- {p[valor]},\t Forma de pagamento- {p["forma de pagamento"]}")
    if op == 3:
        contador = 0
        
        for i in tipos:
            print(f"[{contador}]-{i['tipo']}")
            contador += 1 
            
        ind = input("Escolha o índice do tipo: ") 

        
        
        if ind == "0":
            tipo_buscado = "pista"
        elif ind == "1":
            tipo_buscado = "camarote"
        elif ind == "2":
            tipo_buscado = "VIP"
        else:
            print("Índice inválido")
            continue


        for ingr in ingressos:
            if ingr["tipo"] == tipo_buscado:
                print(f"Comprador- {ingr['nome']},\t Tipo- {ingr['tipo']},\t Valor- {ingr['valor']}")
    if op == 4:
        print(f"Total arrecadado: R$ {receita}")
    if op == 5:
        for i in tipos:
            print(f"Tipo: {i['tipo']} - Restantes: {i['quantidade']}")
    if op == 6:
        print("SAINDO DO SISTEMA")
        break

    
