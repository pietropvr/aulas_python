# Comentários iniciam com # e terminam no final a linha.
# Varáveis possuem vários tipos.
# Nomes de variáveis não podem começar com número, mas podem ter número no meio ou fim.
# Em Python, o tipo não é especificado explicitamente:

preco_original = 150.0  # Número sem ponto é inteiro, com ponto é float (decimal); 
percentual_desconto = 20
moeda = "R$"

valor_do_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_do_desconto

# Para mostrar o resultado, use a função print():
print("Exemplo de cáculo de desconto:")
print(f"Entrada:{moeda}{preco_original:.2f}")

# Escreva: 
# "valor do desconto de xx%: R$XX"
# "Peço final: XX.XX"

print(f"O valor do desconto de {percentual_desconto}%: {moeda} { valor_do_desconto:.2f}") 
print(f"Preço final: R${preco_final:.2f}")