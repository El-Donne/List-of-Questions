# Função que verifica se um número é perfeito.

# Números perfeitos são iguais À SOMA DOS DIVISORES (INCLUINDO ELE MESMO).

def perfectNumbers(x):
    """self_number = x+1""" # Para incluir o número
    cont_var = 0
    for i in range(1, x):
        if x % i == 0:
            cont_var += i
    if cont_var != 0:
        print(f'{x} é um número perfeito\nSoma dos divisores: {cont_var}')
    else:
        print(f'Erro')
        
perfectNumbers(6)