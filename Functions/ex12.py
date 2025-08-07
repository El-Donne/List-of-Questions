# Calcular a soma dos divisores próprios de um número
# Comparar com o número

def comparatorNumberDiv(x):
    sum_numbers = 0
    for i in range(1, x):
        if x % i == 0:
            sum_numbers += i
            
    if sum_numbers == x:
        print(f'{sum_numbers} é igual à {x}')
    elif sum_numbers > x:
        print(f'{sum_numbers} é maior que {x}')
    elif sum_numbers < x:
        print(f'{sum_numbers} é menor que {x}')
        
comparatorNumberDiv(28)