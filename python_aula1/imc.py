# Calculadora IMC
# Solicita peso e altura, entrega IMC (numérico)

# input: imprime texto, coleta dados e o armazena em uma variável:
peso_str = input("Peso (kg):")
altura_str = input("Altura (m):")

#float: converte texto (string) para número com vírgula:
peso = float(peso_str)
altura = float(altura_str)

IMC = peso / (altura ** 2)

print(f"Peso digitado (kg): {peso}")
print(f"Altura digitada (m): {altura}")

print(f"Seu IMC é: {IMC:2f}")


