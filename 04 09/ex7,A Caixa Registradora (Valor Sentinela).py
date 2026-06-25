total=0
valor=float(input("digite o valor do produto: "))

while(valor!=0):
    total += valor #= Total = total + valor 
    valor = float(input("Digite o valor do produto "))

print(f"Valor total da compra : {total}")