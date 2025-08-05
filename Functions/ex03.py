# Criar calculadora com classes

def Multiplicar():
    numbers = []
    contador = 1
    length = int(input('Insira o tamanho desejado: '))
    for i in range(1, length + 1):
        i = float(input(f'Insira o {i}° número: '))
        numbers.append(i)
        contador *= i
        # Necessariamente precisa ser uma variável a parte
    print(numbers)
    print(contador)
        
Multiplicar()