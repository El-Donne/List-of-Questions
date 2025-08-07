# Função que verifica se o número é primo ou não

# Números primos só são divisíveis por 1 e ele mesmo
# Não podem ser 1 nem dois

def primeNumber(x):
    if x <= 1:
        print('ERRO')
    elif x == 2:
        print(f'{x} é primo')
    else:
        for i in range(2, x):
            if x % i == 0:
                print(f'{x} não é primo.')
                break
            else:
                print(f'{x} é primo.')
                break
        print(f'Fim do programa.')
            
primeNumber(5)