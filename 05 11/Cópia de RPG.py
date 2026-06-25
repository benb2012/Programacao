#⚔ Batalha no Dungeon
#Um jogo de RPG em modo texto com listas e dicionários

 
#★★☆
#Dificuldade
#3+
#Monstros
#∞
#Turnos
#Você foi contratado para criar um mini-jogo de RPG em modo texto. O jogador controla um herói que precisa enfrentar 
# monstros em sequência dentro de um dungeon. Cada batalha acontece em turnos: o herói ataca, depois o monstro reage. O jogo termina quando o herói derrota todos os monstros — ou perde toda a vida.
#— ⚔ —
#O que o programa deve ter
#Obrig. Um dicionário representando o herói, com os campos: nome, vida, ataque, defesa e poções.
#Obrig. Uma lista de dicionários com pelo menos 3 monstros, cada um com: nome, vida, ataque e ouro (recompensa).
#Obrig. Sistema de batalha por turnos: herói ataca → monstro contra-ataca. O dano causado desconta a defesa do alvo.
#Obrig. Exibir o status da batalha a cada turno, mostrando a vida atual do herói e do monstro.
#Obrig. Ao derrotar um monstro, somar o ouro ganho ao total acumulado do jogador.
#Extra Antes de atacar, o jogador pode usar uma poção para recuperar vida (respeite o limite de poções no dicionário).
#Extra Ao final, exibir um relatório com: monstros derrotados, ouro acumulado e vida restante do herói.
#— ⚔ —
#Estrutura de dados sugerida
#python · estrutura_inicial.py
# Herói do jogador
#heroi = {
#   "nome":   "Aran",
#  "vida":   100,
# "ataque": 20,
#"defesa": 5,
#"pocoes": 2
#}
 
# Lista de monstros do dungeon
#monstros = [
#    {"nome": "Goblin",    "vida": 30, "ataque": 8,  "ouro": 10},
#    {"nome": "Esqueleto", "vida": 50, "ataque": 12, "ouro": 25},
#    {"nome": "Dragão",    "vida": 80, "ataque": 20, "ouro": 50},
#]
 
#ouro_total = 0
 
# Percorrer cada monstro
#for monstro in monstros:
    # loop de turnos dentro de cada batalha
#    while monstro["vida"] > 0 and heroi["vida"] > 0:
#       # ... (implemente aqui a lógica da batalha)
#        pass
#Dicas de implementação
#Dica 1 — Cálculo de dano
#O dano recebido pode ser calculado como: dano = ataque - defesa. Use max(1, dano) para garantir que o dano mínimo seja sempre 1, mesmo contra inimigos muito resistentes.

#Dica 2 — Loop aninhado
#Use um for para percorrer a lista de monstros. Dentro dele, use um while para controlar os turnos de cada batalha individual.

#Dica 3 — Usando a poção
#Antes de atacar, pergunte ao jogador se quer usar uma poção. Verifique se heroi["pocoes"] > 0 e, ao usar, atualize tanto a vida quanto a quantidade de poções no dicionário.

 
#Utilize apenas os conceitos vistos em aula: dicionários, listas, for, while, if/elif/else e input().
#Que a sorte esteja com seu herói!

#quais monstros tem 
monstros = [
    {"nome": "Goblin",    "vida": 30, "ataque": 8,  "ouro": 10},
    {"nome": "Esqueleto", "vida": 50, "ataque": 12, "ouro": 25},
    {"nome": "Dragão",    "vida": 80, "ataque": 20, "ouro": 50},
]



#heroi e status
print("\t\tPré-visualizaçao do simpleRPG, o futuro melhor RPG")

nome = input("Qual é seu nome guerreiro?: ").title()
if nome =="Edjandir":
    nome= nome+" MELHOR PROFESSOR"

heroi = {
"nome":nome,
"vida":100,
"ataque":20,
"defesa":5,
"pocoes":2,
"ouro": 0
}

print("Heroi:\t Nome :",heroi["nome"],"\t Vida :",heroi["vida"],"\t Ataque :",
      heroi["ataque"],"\t Defesa :",heroi["defesa"],"\t Poções de HP :",heroi["pocoes"],"\t Ouro :",heroi["ouro"] )
print("\n\n==Caçada de monstros==")
for monstro in monstros:
    print(f"{monstro['nome']}: Recompensa de {monstro['ouro']} ouro\n")
    

monstrosmortos=0

for monstro in monstros:
    print("==A BATALHA COMEÇA==\n")
    while monstro['vida'] > 0 and heroi['vida'] > 0:
        

        print ("MONSTRO: "+ monstro["nome"].upper(),"")
        print(f"-STATUS DO MONSTRO-")
        print(f"Vida: {monstro['vida']}\tDano: {monstro['ataque']} - {heroi['defesa']}(defesa do heroi)")

        print(f"--STATUS DO HEROI--\nVida: {heroi['vida']}\t Defesa: {heroi['defesa']}\t Dano: {heroi['ataque']} ")

        print(f"[1]- ATACAR!!({heroi['ataque']} de dano)")
        print(f"[2]- Usar poção de cura(+30 HP)")
        
        
        
        try:
            opb=int(input(f"Oquê você vai fazer,{heroi['nome']}: "))
        except:
            opb=0    

        if opb == 1:
            monstro["vida"]-=heroi["ataque"]
            if monstro["vida"] < 0:
                monstro["vida"] = 0
            print(f"\nVocê atacou o {monstro['nome']}!!, a vida atual dele é {monstro['vida']}")
        elif opb == 2:
            if heroi["pocoes"] > 0:
                heroi["pocoes"]-=1
                heroi["vida"]+=30
                print(f"Você se cura com sucesso!, Sua vida atual é {heroi['vida']}")
                print(f"(Poções:{heroi['pocoes']})")
            else:

                print("Você não tem poções!")    
        elif opb ==777:
            monstro["vida"]-=monstro["vida"]
            print("\n\n\n\n\n\nA insignificante criatura misteriosamente cai morta no chão")    
        elif opb>2 or opb<1:
            print("\n\nVocê se distrai e não faz nada.")

        
        if monstro["vida"]>0:
            dmf=monstro["ataque"]-heroi["defesa"]
            if dmf < 1:
                dmf = 1
            heroi["vida"]-=dmf
            if heroi["vida"] < 0:
                heroi["vida"] = 0
            print(f"\nO {monstro['nome'].upper()} TE ATACA!!, Ele causa {dmf} de dano")
        elif monstro["vida"]<=0:
            monstrosmortos+=1
            heroi["ouro"]+=monstro["ouro"]
            print(f"\nVocê derrota o {monstro['nome']} saqueia seu corpo e segue em frente(ouro atual:{heroi['ouro']})")
            continue
        if heroi["vida"]<=0:
            print(f"VOCÊ MORREU PARA {monstro['nome'].upper()}")   
            break
print(f"\n\nNome: \t{heroi['nome']}")
print(f"Vida final: \t{heroi['vida']}")
print(f"Monstros derrotados:\t{monstrosmortos}")
print(f"Ouro coletado:\t {heroi['ouro']}")
    
    



           

        
                


        
        