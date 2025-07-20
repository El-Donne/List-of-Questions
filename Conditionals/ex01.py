# Número maior, igual ou menor que 10.

num_1 = float(input("Insira um número:\n"))

if (num_1 > 10):
    print(f'O número {num_1} é maior que 10.')
elif (num_1 < 10):
    print(f'O número {num_1} é menor que 10.')
elif (num_1 == 10):
    print(f'O número {num_1} é igual a 10.')
else:
    print('[ERRO]')