palavra = input("Digite uma palavra: ")

for i in range(len(palavra) - 1, -1, -1):
    print(palavra[i], end="")