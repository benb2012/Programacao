estoque = []

def adicionar_produto(estoque):
    id = int(input("Qual o id?: "))
    nome = input("Qual o nome do produto?: ")
    quantidade = int(input("Qual a quantidade?: "))
    preco = float(input("Qual o preço do produto?: "))

    produto = {
        "id": id,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }

    estoque.append(produto)


def listar_estoque(lista):
    print("Estoque de produtos\nID - Nome - Preço - Estoque")
    for produto in lista:
        print(f"{produto['id']} - {produto['nome']} - {produto['preco']} - {produto['quantidade']}")

def atualizar_quantidade(estoque):
    busca_id = int(input("Qual o id do produto? "))
    nova_quantidade = int(input("Qual a nova quantidade? "))

    for i in estoque:
        if i["id"] == busca_id:
            i["quantidade"] = nova_quantidade
            print("Quantidade atualizada!")
            return

    print("Produto não encontrado!")

def calcular_valor_total(estoque):
    soma_total = 0

    for i in estoque:
        soma_total += i["quantidade"] * i["preco"]

    return soma_total