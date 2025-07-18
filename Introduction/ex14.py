# Perguntar quanto ganha por hora;
# Número de horas trabalhadas no mês;
# Desconto de '11%' do Imposto de Renda
# 8% para INSS
# 5% para Sindicato.

print("*"*40)
print("Bem-vindo ao nosso sistema de cálculo de salário líquido!")
print("*"*40)
valor_hora = float(input("Qual o valor que você ganha por hora trabalhada?\n"))
horas_mes = int(input("Quantas horas você trabalhou no mês?"))
salario_bruto = valor_hora * horas_mes
imposto_renda_desconto = salario_bruto * 0.11
# inss_desconto = (salario_bruto - imposto_renda_desconto) * 0.08
# sindicato_desconto = (salario_bruto - imposto_renda_desconto - inss_desconto) * 0.05
# salario_liquido = salario_bruto - imposto_renda_desconto - inss_desconto - sindicato_desconto

"""print(f'Salário bruto: R${salario_bruto}')
print(f'Desconto do IR: R${imposto_renda_desconto}')
print(f'Desconto do INSS: R${inss_desconto}')
print(f'Desconto do Sindicato: R${sindicato_desconto}')
print(f'Salário líquido: R${salario_liquido}')"""

# Versão 2
var_temp = salario_bruto - imposto_renda_desconto
inss_desconto = (var_temp) * 0.08
var_temp = var_temp - inss_desconto
sindicato_desconto = var_temp * 0.05
salario_liquido = var_temp - sindicato_desconto

print(f'Salário bruto: R${salario_bruto}')
print(f'Desconto do IR: R${imposto_renda_desconto}')
print(f'Desconto do INSS: R${inss_desconto}')
print(f'Desconto do Sindicato: R${sindicato_desconto}')
print(f'Salário líquido: R${salario_liquido}')