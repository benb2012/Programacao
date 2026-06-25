
pacientes_graves = 0

while True:

    nome = input("Nome do paciente (ou digite 'encerrar'): ")
    
  
    if nome == "encerrar":
        break
        
  
    gravidade = input("Gravidade (leve, moderada, grave): ")

    if gravidade == "grave":
        print("Atendimento prioritário")
        pacientes_graves = pacientes_graves + 1
    else:
        print("Aguarde na fila")


print("Total de pacientes graves atendidos:", pacientes_graves)