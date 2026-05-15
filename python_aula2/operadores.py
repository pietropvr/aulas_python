nota = float(input("Nota (0-10)"))
freq = float(input("Frequência(%):"))

if nota >= 7 and freq >= 75:
    situacao = "Aprovado"

elif nota < 6 or freq < 70:
    situacao = "Reprovado"

else:
    situacao = "Recuperação"

print(f"Situação do estudante: {situacao}")