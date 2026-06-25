pares=0
impares=0


for i in range (1,6):
   numero= int(input(f"{i}- Digite um número "))

if (numero %2 == 0):
   pares+=1
else:
   impares+=1

print(f"Pares: {pares}\t impares: {impares}")