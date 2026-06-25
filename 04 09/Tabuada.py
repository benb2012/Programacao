

numero = int(input("digite um no. entre 1 e 10 "))
if(numero>1 or numero>10):
    print(f"{numero} é invalido!")
else:
    for i in range (1, 11):
        print(f"{numero}x{i}={numero*i}")