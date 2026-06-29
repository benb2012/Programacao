lista_alunos=[]

def cadastrar_aluno(lista_alunos, nome, turma, nota1, nota2):
    aluno={'nome':nome,
           'turma': turma,
           'nota1': nota1,
           'nota2':nota2}
    lista_alunos.append(aluno)
def calcular_media(aluno):
    media = (aluno['nota1']+aluno['nota2'])/2
    return media 

def listar_alunos(lista_alunos):
    for i in lista_alunos:
        print(f"\nNome: {i['nome']}")
        print(f"Turma: {i['turma']}")
        print(f"Media: {calcular_media(i)}")

def aprovados(lista_alunos):
    
    lista_aprovados = []
    for aluno in lista_alunos:
        if calcular_media(aluno)>=7:
            lista_aprovados.append(aluno)
    return lista_aprovados
            



cadastrar_aluno(lista_alunos, "Ana", "2A", 8, 9)
cadastrar_aluno(lista_alunos, "João", "2A", 6, 6)
cadastrar_aluno(lista_alunos, "Pedro", "2B", 10, 9)

listar_alunos(lista_alunos)

print("\n=== Alunos Aprovados ===")

for aluno in aprovados(lista_alunos):
    print(f"{aluno['nome']} - Média: {calcular_media(aluno)}")
