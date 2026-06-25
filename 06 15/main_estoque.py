from estoque import *

adicionar_produto(estoque)
adicionar_produto(estoque)
adicionar_produto(estoque)

atualizar_quantidade(estoque)

print("\n--- ESTOQUE ATUALIZADO ---")

for produto in estoque:
    print(produto)

print("\nValor total do estoque:")
print(calcular_valor_total(estoque))