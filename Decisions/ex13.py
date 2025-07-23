# Pede um número e verifica se é inteiro ou decimal

valor = float(input('Insira um valor:\n'))
if (valor.is_integer()):
    print('Inteiro')
else:
    print('Decimal')