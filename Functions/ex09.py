# Função que verifica se o número é primo ou não

def primeNumber(x):
    if x % 1 == 0 and x % x == 0:
        print(f'Número {x} é primo.')
    else:
        print(f'Número {x} não é primo.')
        
primeNumber(4)