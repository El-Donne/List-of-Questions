# Pede dois números e qual operação desejada.
# Resultado deve acompanhar se é:
# Par ou ímpar;
# Positivo ou negativo;
# Inteiro ou decimal;

num1 = float(input('Insira o 1° número:\n'))
num2 = float(input('Insira o 2° número:\n'))

operation = input('Qual a operação desejada? \n \
    + \n \
    - \n \
    * \n \
    \ \n')

if (operation == '+'):
    soma = num1 + num2
    print(soma)
    if (soma > 0):
        print('Positivo')
    else:
        print('Negativo')
    if (soma % 2 == 0):
        print('Par')
    else:
        print('Ímpar')
    if (soma.is_integer()):
        print('Inteiro')
    else:
        print('Decimal')
elif (operation == '-'):
    diferenca = num1 - num2
    print(diferenca)
    if (diferenca > 0):
        print('Positivo')
    else:
        print('Negativo')
    if (diferenca % 2 == 0):
        print('Par')
    else:
        print('Ímpar')
    if (diferenca.is_integer()):
        print('Inteiro')
    else:
        print('Decimal')
elif (operation == '*'):
    produto = num1 * num2
    print(produto)
    if (produto > 0):
        print('Positivo')
    else:
        print('Negativo')
    if (produto % 2 == 0):
        print('Par')
    else:
        print('Ímpar')
    if (produto.is_integer()):
        print('Inteiro')
    else:
        print('Decimal')
elif (operation == '/'):
    if (num2 == 0):
        print('NÃO EXISTE DIVISÃO POR ZERO!')
    else:
        divisao = num1 / num2
        print(divisao)
        if (divisao > 0):
            print('Positivo')
        else:
            print('Negativo')
        if (divisao % 2 == 0):
            print('Par')
        else:
            print('Ímpar')
        if (divisao.is_integer()):
            print('Inteiro')
        else:
            print('Decimal')