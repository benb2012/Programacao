from estoque import *

while True:
    print("[1]- adicionar produtos\n" \
    "[2]- Listar estoque\n"\
    "[3]- Atualizar quantidade\n" \
    "[4]- Verificar valor total\n" \
    "[5]- Sair")
    opcao = int(input("Escolha: "))

    if opcao == 1:
        adicionar_produto(estoque)
    elif opcao == 2:
        listar_estoque(estoque)
    
    elif opcao == 3:
        atualizar_quantidade(estoque)
    
    
    
    elif opcao == 4:

        print("\n--- ESTOQUE ATUAL ---")
        for produto in estoque:
            
            print(f"ID: {produto['id']} | Nome: {produto['nome']} | Qtd: {produto['quantidade']} | Preço: R$ {produto['preco']:.2f}")

        print("\nValor total do estoque:")
        total = calcular_valor_total(estoque)
        print(f"R$ {total:.2f}\n")

    elif opcao == 5:
        break
    else:
        print("Opção invalida")