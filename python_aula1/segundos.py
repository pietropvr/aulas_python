# Divisão inteira (módulo)

valor1 = 10
valor2 = 3

div = valor1 / valor2
mod = valor1 // valor2

print(f"Divisão: {valor1}/{valor2}={div}")
print(f"Divisão inteira: {valor1}//{valor2}={mod}")


# Receba o número de segundos do usuário
# Calcule horas, minutos e segundos usando // e %
# Exiba no formato HH:MM:SS, use var:02d para formato

total_segundos= int(input("Insira os segundos aqui:"))

hora = total_segundos // 3600
resto_segundos = total_segundos % 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60

print(f"Resultado: {hora:02d}:{minutos:02d}:{segundos:02d}")
