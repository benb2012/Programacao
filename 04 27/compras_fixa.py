#Crie uma lista de compras com produtos
#Cada produto tera nome , preço, quantidade
#Mostre todos os produtos da lista e o valor total da compra
valor_total=0
compras = [
    {"Produto": "Arroz", "valor": 7.50, "Quantidade": 2},
    {"Produto": "Leite", "valor": 5.20, "Quantidade": 4},
    {"Produto": "Ovos", "valor": 1.00, "Quantidade": 12},
    {"Produto": "Café ", "valor": 18.90, "Quantidade": 2},
    {"Produto": "Pão", "valor": 0.70, "Quantidade": 10},
    ]
print("\t\t--lista de compras--")
for comida in compras:
    print("Produto -",comida["Produto"],"----Valor -",comida['valor'],"----Quantidade -",comida['Quantidade'])
    

for jorje in compras:
    valor_produto= jorje['valor'] * jorje['Quantidade']
    valor_total+= valor_produto
print(f"---O valor total é R${valor_total}---")
