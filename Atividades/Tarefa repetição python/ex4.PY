palavra = input("Digite uma palavra: ")

contador = 0

for letra in palavra:
    if letra in "aeiouAEIOU":
        contador += 1

print("Quantidade de vogais:", contador)