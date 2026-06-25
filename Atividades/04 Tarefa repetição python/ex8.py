quantidade = int(input("Quantos itens você quer adicionar? "))

lista = []

for i in range(quantidade):
    item = input("Digite o nome do item: ")
    lista.append(item)

print("Lista de compras:", lista)
