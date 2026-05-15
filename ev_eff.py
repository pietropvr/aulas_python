dist = float(input("Distância do trajeto (km): "))
consumo_mj_km = float(input("Consumo do veículo (MJ/km): "))
preco_kwh = float(input("Preço do kwh (R$):"))

consumo_kwh_km = consumo_mj_km / 3.6 #Fator de conversão de MJ par kwm" 

energia_total = dist*consumo_kwh_km
custo_total = energia_total * preco_kwh
custo_por_km = custo_total / dist

print(f"Energia usada: {energia_total:.2f}")
print(f"Custo por trajeto: {custo_total:.2f}")
print(f"Custo por km: {custo_por_km:.2f}")
