total = 0

while True:
    nome = input("Digite o nome do livro (ou 'finalizar'): ")

    if nome == "finalizar":
        break

    preco = float(input("Digite o preço do livro: "))

    if preco > 100:
        resposta = input("Livro caro, deseja continuar? (s/n): ").lower()

        if resposta == "s":
            total += preco
            print("Livro adicionado ao carrinho")

        elif resposta == "n":
            print("Livro NÃO adicionado")

        else:
            print("Resposta inválida, livro NÃO adicionado")

    else:
        print("Livro adicionado ao carrinho")
        total += preco

print("Total da compra: R$", total)