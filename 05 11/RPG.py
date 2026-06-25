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

nome = input("Qual é seu nome guerreiro?: ").upper()
if nome =="EDJANDIR":
    nome= nome+" MELHOR PROFESSOR"

heroi = {
"nome":nome+" O PROGRAMADOR",
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



for monstro in monstros:
    while monstro['vida'] > 0 and heroi['vida'] > 0:
        print("==A BATALHA COMEÇA==\n")

        print ("MONSTRO: "+ monstro["nome"].upper(),"")
        print(f"-STATUS DO MONSTRO-")
        print(f"Vida: {monstro["vida"]}\tDano: {monstro["ataque"]}")

        print(f"--STATUS DO HEROI--\nVida: {heroi["vida"]}\t Defesa: {heroi['defesa']}\t Dano: {heroi['ataque']} ")

        
        break