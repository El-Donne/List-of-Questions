# Verificar se um número está dentro de um intervalo

def verifyNumber():
    number = float(input('Insira o número: '))
    if 0 < number < 100:
        print('Está dentro do intervalo de 0-100!')
    else:
        print('Não está dentro do intervalo.')
        
verifyNumber()