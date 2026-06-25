
# Exercício 2: Biblioteca de Jogos

#Organiza uma coleção de jogos de PC ou celular, ajudando no controle dos jogos instalados e do tempo de diversão:
#Crie uma função para registrar jogos com nome, plataforma (PC, Android, iOS, etc.), gênero e status (instalado ou não).
#Crie uma função que lista todos os jogos cadastrados.
#Crie uma função para filtrar jogos instalados e os que ainda não foram instalados.
#Crie uma função para calcular a quantidade total de jogos cadastrados e quantos estão instalados.
#Situação extra: permitir marcar jogos como “instalados” e atualizar automaticamente o status.





jogos = []

def registrar():

    print("\n-- REGISTRAR JOGO --")

    nome = input("Nome: ")
    plataforma = input("Plataforma: ")
    genero = input("Gênero: ")

    jogo = {
        "nome": nome,
        "plataforma": plataforma,
        "genero": genero,
        "instalado": False
    }

    jogos.append(jogo)

    print("Jogo cadastrado!")

def listar():

    if len(jogos) == 0:
        print("Nenhum jogo cadastrado.")
        return

    print("\n-- TODOS OS JOGOS --")

    for jogo in jogos:

        print(
            f"Nome: {jogo['nome']}, "
            f"Plataforma: {jogo['plataforma']}, "
            f"Gênero: {jogo['genero']}, "
            f"Instalado: {jogo['instalado']}"
        )

def filtro():

    print("\n-- INSTALADOS --")

    for jogo in jogos:

        if jogo["instalado"]:
            print(jogo)

    print("\n-- NÃO INSTALADOS --")

    for jogo in jogos:

        if not jogo["instalado"]:
            print(jogo)

def quantidade():

    total = 0
    instalados = 0

    for jogo in jogos:

        total += 1

        if jogo["instalado"]:
            instalados += 1

    print(f"\nTotal de jogos: {total}")
    print(f"Jogos instalados: {instalados}")
    print(f"Jogos não instalados: {total - instalados}")

def instalar():

    encontrou = False

    print("\n-- JOGOS NÃO INSTALADOS --")

    for i in range(len(jogos)):

        if not jogos[i]["instalado"]:

            print(f"[{i}] {jogos[i]['nome']}")
            encontrou = True

    if not encontrou:
        print("Todos os jogos já estão instalados.")
        return

    indice = int(input("Escolha o índice do jogo: "))

    if 0 <= indice < len(jogos):

        jogos[indice]["instalado"] = True

        print("Jogo marcado como instalado!")

    else:
        print("Índice inválido!")

while True:

    print("\n--- BIBLIOTECA DE JOGOS ---")
    print("1 - Registrar jogo")
    print("2 - Listar jogos")
    print("3 - Filtrar jogos")
    print("4 - Quantidade de jogos")
    print("5 - Marcar como instalado")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        registrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        filtro()

    elif opcao == "4":
        quantidade()

    elif opcao == "5":
        instalar()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")