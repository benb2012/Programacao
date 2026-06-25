import random

numero_secreto = random.randint(1, 20)

palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Digite um número entre 1 e 20: "))

    if palpite < numero_secreto:
        print("Maior")
    elif palpite > numero_secreto:
        print("Menor")
    else:
        print("Acertou!")
        