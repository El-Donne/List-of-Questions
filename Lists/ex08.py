# Vetor de 5 números inteiros
# Soma, produto e os números
numeros = []
soma = 0
produto = 1 # Se for zero, anula a operação
for i in range(1, 6):
    vetor = int(input(f'{i}° número: '))
    numeros.append(vetor)
    soma += i
    produto *= i
    # Essas duas variáveis PRECISAM SER DECLARADAS ANTES
print(numeros)
print(soma)
print(produto)