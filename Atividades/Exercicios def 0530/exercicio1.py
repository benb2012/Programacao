#Exercício 1: Controle de Produção de Vídeos

#Organiza o processo de criação de conteúdo para redes sociais ou YouTube, ajudando no planejamento e acompanhamento das produções:
#Crie uma função para registrar vídeos com título, tema, duração estimada e status (gravado ou não).
#Crie uma função que lista todos os vídeos planejados.
#Crie uma função para filtrar vídeos já gravados e os que ainda estão pendentes.
#Crie uma função para calcular o tempo total de conteúdo planejado e o tempo já gravado.
#Situação extra: permitir marcar vídeos como “gravados” e atualizar automaticamente o status.

videos=[]

def registrar():
    print ("-- REGISTRAR VIDEO --\n")
    titulo = input("Qual vai ser o titulo?")
    tema = input("Qual vai ser o tema?")
    duracao = int(input("Qual vai ser a duração?(em minutos)"))

    video={
        "titulo":titulo,
        "tema":tema,
        "duracao":duracao,
        "gravado":False

    }
    videos.append(video)
    
def listar():
    encontrou = False
    for video in videos:
        
            print(f"Titulo: {video['titulo']}, Tema: {video['tema']}, Duração(em minutos): {video['duracao']}, Gravado: {video['gravado']}")
            encontrou = True
    

def filtro():
    
    print("--Gravados--\n")
    
    for video in videos:
        if video["gravado"]:
            
            print(f"{video}\n")
    print("--Pendente--")
    for video in videos:
        
            if not video["gravado"]:
                print(f"{video}\n")

def tempo():
    tm = 0
    tg = 0
    for i in videos:
        

        tm += i["duracao"]
    
        if i["gravado"]:
            tg += i["duracao"]
    
    tp = tm - tg


    print(f"Tempo maximo(em minutos): {tm}\n")
    print(f"Tempo gravado(em minutos): {tg}\n")
    print(f"Tempo pendente(em minutos): {tp}\n") 

def marcar():
    
    encontrou = False
    for i in range(len(videos)):
        if not videos[i]["gravado"]:
            print(f"[{i}]Titulo: {videos[i]['titulo']}, Gravado: {videos[i]['gravado']}\n ")
            
            encontrou= True
    
            
        
    if encontrou == False:
            print("Não há nenhum video pendente")
            return 
        
    ind = int(input("Escolha:"))
            
    videos[ind]["gravado"]= True

    print("Video finalizado")

while True:

    print("\n--- CONTROLE DE VIDEOS ---")
    print("1 - Registrar vídeo")
    print("2 - Listar ")
    print("3 - Filtrar vídeos")
    print("4 - Calcular tempos")
    print("5 - Marcar como gravado")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        registrar()

    elif opcao == "2":
        listar()

    elif opcao == "3":
        filtro()

    elif opcao == "4":
        tempo()

    elif opcao == "5":
        marcar()

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida")