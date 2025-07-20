# Pede dois números e imprime o maior deles

num1 = float(input("Insira o 1° número:\n"))
num2 = float(input("Insira o 2° número:\n"))

if (num1 > num2):
    print(f'Maior número: {num1}')
else:
    print(f'Maior número: {num2}')
    
# OBS.:
# Considerando um conjunto com elementos maior que dois, devemos encontrar uma forma de fazer o cálculo automaticamente para agilizar o processo.
# Isso pode ser possível usando dados de armazenamento e funções matemáticas providas de alguma biblioteca.