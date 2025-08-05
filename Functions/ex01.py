# Criar função que dá a máxima de três números
"""
def numberMax(x, y, z):
    lista = []
    lista.append(x)
    lista.append(y)
    lista.append(z)
    MaxofThree = max(lista)
    print(f'Máximo dos três números de {lista}:\n{MaxofThree}')
    return MaxofThree # SEMPRE NO FINAL

numberMax(1, 2, 3)
"""

def MaximaNumeros():
    numeros = []
    tamanho = int(input('De quantos números você deseja saber a máxima?\n'))
    for i in range(1, tamanho + 1):
        i = float(input(f'Insira o {i}° número:'))
        numeros.append(i)
    maxima_dos_tres = max(numeros)
    print(f'Máxima da lista de números {numeros}:\n{maxima_dos_tres}')
    
MaximaNumeros()