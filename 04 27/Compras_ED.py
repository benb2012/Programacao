#Crie uma lista de compras com produtos
#Cada produto terá nome, preço, quantidade
#Mostre todos os produtos da lista e o valor total da compra
produtos = []
valor_total = 0

while (True):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: "))
    quantidade = int(input("Digite a quantidade: "))
    valor_total += (preco * quantidade)

    produtos.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})

    continua = input("Deseja continuar (Sim)-S (Não)-Qualquer tecla: ")
    if continua.upper() != "S":
        break

print("Sua compra...")
for produto in produtos:
    print(f"Produto: {produto['nome']}", f"Preço: {produto['preco']}",
          f"Quantidade: {produto['quantidade']}")
print(f"Valor total: {valor_total}")    