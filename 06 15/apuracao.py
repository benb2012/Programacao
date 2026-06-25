apuracao = {
    "Ana": 0,
    "Pedro": 0,
    "Lucas": 0,
    "Maria": 0
}

def computar_voto(apuracao):
    nome = input("Digite o nome do candidato: ")

    if nome in apuracao:
        apuracao[nome] += 1
        print("Voto computado!")
    else:
        print("Candidato não existe!")

def obter_vencedor(apuracao):
    vencedor = ""
    maior = -1

    for candidato in apuracao:
        if apuracao[candidato] > maior:
            maior = apuracao[candidato]
            vencedor = candidato

    return vencedor

def gerar_relatorio(apuracao):
    total = sum(apuracao.values())

    relatorio = []

    for candidato in apuracao:
        if total > 0:
            porcentagem = (apuracao[candidato] / total) * 100
        else:
            porcentagem = 0

        relatorio.append([candidato, porcentagem])

    return relatorio