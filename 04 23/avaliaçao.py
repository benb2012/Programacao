notas =[]
soma=0
while(True):
    nota = int(input("Digite uma nota: "))
    if(nota <0):
        break
    elif(nota<0):
        continue
    else:
        notas.append(nota)

if(len(notas)==0):
    print("Não ha notas na avaliação")
else:
    menor=notas[0]
    maior=notas[0]
for nota in notas:

     if nota< menor:
            menor = nota
     if nota > maior:
             maior = nota
soma+= nota
print("A media da notas é ",(soma/len(notas)))
print(f"A menor nota é {menor}")
print(f"A maior nota é {maior}")