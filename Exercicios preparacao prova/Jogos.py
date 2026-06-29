lista_jogos=[]

def cadastrar_jogos(lista_jogos, nome, genero, horas):
    jogo={
        "nome":nome,
        "genero":genero,
        "horas":horas
    }
    lista_jogos.append(jogo)

def listar (lista_jogos):
    for i in lista_jogos:
        print(f"\nNome: {i["nome"]}\n" 
              f"Gênero: {i["genero"]}\n"
              f"Horas jogadas: {i["horas"]}")
        
def calcular_total_horas(lista_jogos):
    total=0
    for i in lista_jogos:
        total += i["horas"]
    return total

def jogo_mais_jogado(lista_jogos):
    maior = lista_jogos[0]
    for i in lista_jogos:
        if i["horas"]> maior["horas"]:
            maior = i
    return maior
    
    





cadastrar_jogos(lista_jogos, "Minecraft", "Sandbox", 120)
cadastrar_jogos(lista_jogos, "Valorant", "FPS", 80)
cadastrar_jogos(lista_jogos, "Terraria", "Sandbox", 95)
    
    
listar(lista_jogos)

print(f"\nTotal de horas jogadas: {calcular_total_horas(lista_jogos)}")

mais_jogado = jogo_mais_jogado(lista_jogos)

print("\n=== Jogo Mais Jogado ===")
print("Nome:", mais_jogado["nome"])
print("Horas:", mais_jogado["horas"])