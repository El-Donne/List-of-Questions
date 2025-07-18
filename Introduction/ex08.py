# Perguntar ao usuário quanto ele ganha por hora e número de horas trabalhadas por mês.
# Calcular e mostrar o total do salário no mês.

# Versão 1
print("*"*20)
print("Bem-vindo ao sistema J2R!")
print("*"*20)

ganho_hora = float(input("Quanto você ganha por hora?\n\t"))
horas_trabalhadas = int(input("Quantas horas você trabalha por mês?\n\t"))

# print(f"Você trabalha {horas_trabalhadas}h por mês e ganha R${ganho_hora} por hora,\n o que dá um total de {horas_trabalhadas*ganho_hora}")

# Versão 2
calculo = horas_trabalhadas * ganho_hora
print(f"Salário do funcionário: R${calculo}")