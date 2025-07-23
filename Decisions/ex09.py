# Pedir três lados de um triângulo

side1 = float(input('Insira o valor do 1° lado:\n'))
side2 = float(input('Insira o valor do 2° lado:\n'))
side3 = float(input('Insira o valor do 3° lado:\n'))

if (side1+side2>side3 or side1+side3>side2 or side2+side3>side1):
    print('Triângulo formado com sucesso!')
    if (side1 == side2 == side3):
        print('Tipo de triângulo: equilátero.')
    elif (side1 == side2 or side2 == side3 or side1 == side3):
        print('Tipo de triângulo: Isóceles')
    elif (side1 != side2 != side3):
        print('Tipo de triângulo: escaleno')
    else:
        print('[ERRO]')
else:
    print('[ERRO]')
    
# Versão 2
# Dá para armazenar os dados em uma lista, percorrer todos os itens e fazer a comparação

list = []
list.append(side1)
list.append(side2)
list.append(side3)
