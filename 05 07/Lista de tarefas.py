# 📝 Exercício 3: Lista de Tarefas (To-Do List)
# Crie um programa que permita:

# Adicionar tarefas com descrição e status (pendente ou concluída).
# Listar todas as tarefas.
# Marcar uma tarefa como concluída.
# Filtrar apenas as tarefas pendentes.
# Dica: Use uma lista de dicionários para armazenar as tarefas.

tarefas = []
while(True):
    print("---TAREFAS---\n [1] Adicionar tarefa\n [2] listar tarefas\n [3] listar tarefas pendentes")

    opcao = int(input("Escolha uma opção: "))
    