import random


filmes = [
    
        {"id": 1,"titulo": "Harry Potter e a Pedra Filosofal"},
        

    
    
       { "id": 2, "titulo": "Os Vingadores Guerra infinita"},
       
        
    
       { "id": 3, "titulo": "Homem de Ferro"}
       
        
    
]

album =[{'id': 1, 'filmeid' : 1, "valor" : 20},
        {'id': 2, 'filmeid' : 2, "valor" : 20},
        {'id': 3, 'filmeid' : 3, "valor" : 20}
          
]

pacotes = [

    {"id": 1, "filmeid": 1, "valor": 4},
    {"id": 2, "filmeid": 2, "valor": 4},
    {"id": 3, "filmeid": 3, "valor": 4}]


figurinhas = [
    # --- Filme 1: Harry Potter e a Pedra Filosofal ---
    {"id": 1,  "id_filme": 1, "personagem": "Harry Potter"},
    {"id": 2,  "id_filme": 1, "personagem": "Hermione Granger"},
    {"id": 3,  "id_filme": 1, "personagem": "Rony Weasley"},
    {"id": 4,  "id_filme": 1, "personagem": "Alvo Dumbledore"},
    {"id": 5,  "id_filme": 1, "personagem": "Lord Voldemort"},
    {"id": 6,  "id_filme": 1, "personagem": "Severo Snape"},
    {"id": 7,  "id_filme": 1, "personagem": "Rúbeo Hagrid"},

    # --- Filme 2: Os Vingadores ---
    {"id": 8,  "id_filme": 2, "personagem": "Homem de Ferro"},
    {"id": 9,  "id_filme": 2, "personagem": "Capitão América"},
    {"id": 10, "id_filme": 2, "personagem": "Thor"},
    {"id": 11, "id_filme": 2, "personagem": "Hulk"},
    {"id": 12, "id_filme": 2, "personagem": "Viúva Negra"},
    {"id": 13, "id_filme": 2, "personagem": "Gavião Arqueiro"},
    {"id": 14, "id_filme": 2, "personagem": "Loki"},

    # --- Filme 3: Homem de Ferro ---
    {"id": 15, "id_filme": 3, "personagem": "Tony Stark"},
    {"id": 16, "id_filme": 3, "personagem": "Pepper Potts"},
    {"id": 17, "id_filme": 3, "personagem": "James Rhodes (Rhodey)"},
    {"id": 18, "id_filme": 3, "personagem": "Monstro de Ferro (Obadiah Stane)"},
    {"id": 19, "id_filme": 3, "personagem": "JARVIS"},
    {"id": 20, "id_filme": 3, "personagem": "Happy Hogan"},
    {"id": 21, "id_filme": 3, "personagem": "Nick Fury"}
]   

valort=0
qnta=0
valortp=0
qntp = 0

itenscomp = []
while True:
    print("(1)- Comprar album\n (2)- Comprar pacote de figurinhas\n (3)- Encerrar")
    op=int(input("-->"))

    if op ==1:
        print("Escolha o filme (id):")
        for i in filmes :
            print(i["id"] , i["titulo"])
        opf = int(input("ID:"))
        qnt = int(input("Quantidade:"))
        encontrou = False
        for i in album:
            
            if opf == i["filmeid"]:
                itenscomp.append({
                    "tipo": "Album",
                    "filme": i["filmeid"],
                    "quantidade": qnt,
                    "valor": i["valor"]*qnt})
                valort += i["valor"]*qnt
                qnta += qnt
                print( "album comprado com sucesso")
                encontrou = True
                break
        if encontrou== False:
            print("erro, id inexistente")

    elif op ==2:
        print("Escolha o filme (id):")
        for i in filmes :
                print(i["id"] , i["titulo"])
        opf = int(input("ID:"))
        qnt = int(input("Quantidade:"))
        encontrou = False
        for i in pacotes:
                
                if opf == i["filmeid"]:
                    itenscomp.append({
                        "tipo": "pacote",
                        "filme": i["filmeid"],
                        "quantidade": qnt,
                        "valor": i["valor"]*qnt})
                    valortp += i["valor"]* qnt
                    qntp += qnt

                    print( "pacote comprado com sucesso, A revelação das figurinhas será feita no final da compra")
                    encontrou = True
                    break
        if encontrou == False:
                print("erro, id inexistente")
    elif op==3:
        conseguidas = []

        print("Vamos abrir os pacotes:")
        for i in itenscomp:
            if i["tipo"] == "pacote":
            
                print("\nPacotes do filme", i["filme"])

                for pacote in range(i["quantidade"]):

                    print("Pacote", pacote + 1)

                    for figurinha in range(4):

                        sorteada = random.choice(figurinhas)

                        while sorteada["id_filme"] != i["filme"]:
                            sorteada = random.choice(figurinhas)

                        conseguidas.append(sorteada)

                        print("-", sorteada["personagem"])

        print("Resultado da Compra:")
        desconto = 0
        if qntp> 10:
            desconto = valortp*0.10
        elif qntp> 5:
            desconto = valortp*0.05
        total = valort + valortp - desconto

        print("\n========== RESUMO DA COMPRA ==========")

        for item in itenscomp:
            print(item)

        print("Figurinhas conseguidas")
        for i in conseguidas:
            print(i["personagem"])

        print("\nValor dos álbuns: R$", valort)
        print("Valor dos pacotes: R$", valortp)
        print("Desconto: R$", desconto)
        print("TOTAL: R$", total)

        break

    else:
        print("Opção inválida.")


                         
                






    
        





    