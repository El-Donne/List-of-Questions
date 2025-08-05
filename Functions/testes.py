# Criar calculadora com classes

def Multiplicar():
    numbers = []
    length = int(input('Insira o tamanho desejado: '))
    for i in range(1, length + 1):
        i = float(input(f'Insira o {i}° número: '))
        i *= i
        # Nesse caso não funciona porque o laço 'for' junto do 'input' reinicia a variável a cada novo valor atribuído
    numbers.append(i)
    
    print(numbers)
        
Multiplicar()