# Somar todos os itens de uma lista

def SomaNumeros():
    numeros = []
    tamanho = int(input('Quantos números deseja somar?\n'))
    for i in range(1, tamanho + 1):
        i = float(input(f'Insira o {i}° número: '))
        numeros.append(i)
    resultado = sum(numeros)
    """return resultado"""
    print(resultado)
    
SomaNumeros()