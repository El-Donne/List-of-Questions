# Pede um vetor A com 10 números inteiros
# Calcula e mostra a soma dos quadrados
from math import sqrt

squares = []
sum_var = 0

for i in range(1, 11):
    num_int = int(input(f'Insira o {i}° número: '))
    sum_var += sqrt(num_int)
    squares.append(sum_var)
print(squares)