# Cálculo da folha de pagamento;
# Descontos do imposto de renda; dependem do SALÁRIO BRUTO;
# 3% do Sindicato e 11% de depósito do FGTS;
# salário de 900 é isento; 1500: 5%; 2500: 10%; 2500<: 20;

# Imprimir salário, IR, INSS, FGTS, descontos e salário líquido.

print("*"*50)
print("BEM-VINDO AO SISTEMA DE CÁLCULO DE\nFOLHA DE PAGAMENTO!")
print("*"*50)

hora_trabalhada = int(input('Quantidade de horas trabalhadas:\n'))
valor_hora = int(input('Valor da hora:\n'))
salario_bruto = hora_trabalhada * valor_hora
if (salario_bruto <= 900):
    print(f'Salário bruto:\t R${salario_bruto}')
    print('Você está ISENTO de descontos.')
elif (900 < salario_bruto <= 1500):
    print(f'Salário bruto:\t R${salario_bruto}')
    imposto_renda = salario_bruto * 0.05
    print(f'IR ({0.05*100}%)\t R${imposto_renda}')
    inss = salario_bruto * 0.10
    print(f'INSS ({0.10*100}%)\t R${inss}')
    print(f'FGTS (11%)\t R${salario_bruto*0.11}\nNão será descontado do seu salário.\n')
    print(f'Descontos:\t R${imposto_renda+inss}')
    salario_liquido = salario_bruto - imposto_renda - inss
    print(f'Salário líquido:\t R${salario_liquido}')
elif (1500 < salario_bruto <= 2500):
    print(f'Salário bruto: R${salario_bruto}')
    imposto_renda = salario_bruto * 0.10
    print(f'IR ({0.10*100}%)\t R${imposto_renda}')
    inss = salario_bruto * 0.10
    print(f'INSS ({0.10*100}%)\t R${inss}')
    print(f'FGTS (11%)\t R${salario_bruto*0.11}\nNão será descontado do seu salário.\n')
    print(f'Descontos:\t R${imposto_renda+inss}')
    salario_liquido = salario_bruto - imposto_renda - inss
    print(f'Salário líquido:\t {salario_liquido}')
elif (salario_bruto >2500):
    print(f'Salário bruto:\t R${salario_bruto}')
    imposto_renda = salario_bruto * 0.20
    print(f'IR ({0.20*100})\t R${imposto_renda}')
    inss = salario_bruto * 0.10
    print(f'INSS ({0.10*100}%)\t R${inss}')
    print(f'FGTS (11%):\t R${salario_bruto*0.11}\nNão será descontado do seu salário.\n')
    print(f'Descontos:\t R${imposto_renda+inss}')
    salario_liquido = salario_bruto - inss - imposto_renda
    print(f'Salário líquido:\t R${salario_liquido}')
else:
    print('[ERRO]')