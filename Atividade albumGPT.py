import random

filmes = [

    {"id": 1, "titulo": "Harry Potter e a Pedra Filosofal"},
    {"id": 2, "titulo": "Os Vingadores Guerra Infinita"},
    {"id": 3, "titulo": "Homem de Ferro"}

]

album = [

    {"id": 1, "filmeid": 1, "valor": 20},
    {"id": 2, "filmeid": 2, "valor": 20},
    {"id": 3, "filmeid": 3, "valor": 20}

]

pacotes = [

    {"id": 1, "filmeid": 1, "valor": 4},
    {"id": 2, "filmeid": 2, "valor": 4},
    {"id": 3, "filmeid": 3, "valor": 4}

]

figurinhas = [

    {"id": 1, "id_filme": 1, "personagem": "Harry Potter"},
    {"id": 2, "id_filme": 1, "personagem": "Hermione Granger"},
    {"id": 3, "id_filme": 1, "personagem": "Rony Weasley"},
    {"id": 4, "id_filme": 1, "personagem": "Alvo Dumbledore"},
    {"id": 5, "id_filme": 1, "personagem": "Lord Voldemort"},
    {"id": 6, "id_filme": 1, "personagem": "Severo Snape"},
    {"id": 7, "id_filme": 1, "personagem": "Rúbeo Hagrid"},

    {"id": 8, "id_filme": 2, "personagem": "Homem de Ferro"},
    {"id": 9, "id_filme": 2, "personagem": "Capitão América"},
    {"id": 10, "id_filme": 2, "personagem": "Thor"},
    {"id": 11, "id_filme": 2, "personagem": "Hulk"},
    {"id": 12, "id_filme": 2, "personagem": "Viúva Negra"},
    {"id": 13, "id_filme": 2, "personagem": "Gavião Arqueiro"},
    {"id": 14, "id_filme": 2, "personagem": "Loki"},

    {"id": 15, "id_filme": 3, "personagem": "Tony Stark"},
    {"id": 16, "id_filme": 3, "personagem": "Pepper Potts"},
    {"id": 17, "id_filme": 3, "personagem": "James Rhodes"},
    {"id": 18, "id_filme": 3, "personagem": "Obadiah Stane"},
    {"id": 19, "id_filme": 3, "personagem": "JARVIS"},
    {"id": 20, "id_filme": 3, "personagem": "Happy Hogan"},
    {"id": 21, "id_filme": 3, "personagem": "Nick Fury"}

]

valor_total_albuns = 0
valor_total_pacotes = 0
quantidade_pacotes = 0

itens_comprados = []

while True:

    print("\n1 - Comprar álbum")
    print("2 - Comprar pacote de figurinhas")
    print("3 - Finalizar compra")

    opcao = int(input("--> "))

    if opcao == 1:

        print("\nFilmes disponíveis:")

        for filme in filmes:
            print(filme["id"], "-", filme["titulo"])

        id_filme = int(input("Escolha o id do filme: "))

        filme_encontrado = False

        for album_atual in album:

            if id_filme == album_atual["filmeid"]:

                itens_comprados.append({
                    "tipo": "Album",
                    "filme": id_filme,
                    "valor": album_atual["valor"]
                })

                valor_total_albuns += album_atual["valor"]

                print("Álbum comprado com sucesso!")

                filme_encontrado = True
                break

        if filme_encontrado == False:
            print("Filme não encontrado.")

    elif opcao == 2:

        print("\nFilmes disponíveis:")

        for filme in filmes:
            print(filme["id"], "-", filme["titulo"])

        id_filme = int(input("Escolha o id do filme: "))
        quantidade = int(input("Quantos pacotes deseja comprar? "))

        filme_encontrado = False

        for pacote in pacotes:

            if id_filme == pacote["filmeid"]:

                filme_encontrado = True

                valor_total_pacotes += pacote["valor"] * quantidade
                quantidade_pacotes += quantidade

                itens_comprados.append({
                    "tipo": "Pacote",
                    "filme": id_filme,
                    "quantidade": quantidade,
                    "valor": pacote["valor"] * quantidade
                })

                print("\nFigurinhas recebidas:")

                lista_figurinhas = []

                for figurinha in figurinhas:

                    if figurinha["id_filme"] == id_filme:
                        lista_figurinhas.append(figurinha)

                for pacote_comprado in range(quantidade):

                    print("\nPacote", pacote_comprado + 1)

                    for figurinha in range(4):
                        sorteada = random.choice(lista_figurinhas)
                        print("-", sorteada["personagem"])

                break

        if filme_encontrado == False:
            print("Filme não encontrado.")

    elif opcao == 3:

        desconto = 0

        if quantidade_pacotes > 10:
            desconto = valor_total_pacotes * 0.10

        elif quantidade_pacotes > 5:
            desconto = valor_total_pacotes * 0.05

        total = valor_total_albuns + valor_total_pacotes - desconto

        print("\n========== RESUMO DA COMPRA ==========")

        for item in itens_comprados:
            print(item)

        print("\nValor dos álbuns: R$", valor_total_albuns)
        print("Valor dos pacotes: R$", valor_total_pacotes)
        print("Desconto: R$", desconto)
        print("TOTAL: R$", total)

        break

    else:
        print("Opção inválida.")