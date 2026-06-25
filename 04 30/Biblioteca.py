#criar uma aplicaçao simples para cadastrar livros 
#cada livro tem titilo, autor, ano_publicaçao,disponivel
#usar dicionario para representar cada livro 
#usar a lista para guardar uma lista de livros
#adicionar livros na lista 
#listar todos os livros
livros=[]
while (True):
    titulo = input("Digite o titulo do livro: ")
    autor = input("Digite o autor: ")
    ano_publicacao = int(input("Digite o ano da publicação do livro: "))
    disponivel= input("O livro esta disponivel?(S/N)")
    disponivel= disponivel.upper()=="S"

    livros.append({'titulo': titulo, 'autor': autor, 'ano_publicacao': ano_publicacao, 'disponivel': disponivel})
    continua = input("Deseja continuar?(S/N)")
    if continua.upper() != "S":
        break
for i in livros:
    print(f"Titulo:{i['titulo']}", f"Autor:{i['autor']}", f"Ano da publicação:{i['ano_publicacao']}", f"Disponivel:{i['disponivel']}")