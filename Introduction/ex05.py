# Converter metros em centímetros
# 1m = 100cm

# Versão 1
medida_metro = float(input("Insira sua medida em metros:\n"))
print("Medida transformada em centímetros com sucesso!")
print(int(medida_metro*100), "cm")

# Versão 2
conversao = int(medida_metro * 100)
# O "int" converte o resultado da operação para número inteiro.

print(conversao)