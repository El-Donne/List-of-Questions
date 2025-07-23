# Calcular equações de segundo grau.
import math

print('Programa inicializado com sucesso!')
print('*'*60)
print('BEM-VINDO AO SISTEMA DE CÁLCULO DE\nEQUAÇÃO DO SEGUNDO GRAU!')
print('*'*60)

a = float(input('Informe o valor de A:\n'))
b = float(input('Informe o valor de B:\n'))
c = float(input('Informe o valor de C:\n'))

print(f'{a}x² + {b}x + {c}')

if (a == 0):
    print('Não é uma equação do 2° grau.')
else:
    ## Usando delta
    delta = b**2 -4*a*c
    if (delta < 0):
        print('Não possui raízes reais.')
        exit()
    elif (delta > 0):
        raiz_delta = math.sqrt(delta)
        x1 = (-b+raiz_delta)/2
        x2 = (-b-raiz_delta)/2
        print(f'Raízes: {x1, x2}.')
    elif (delta == 0):
        raiz_delta = math.sqrt(delta)
        x1 = (-b+raiz_delta)/2
        x2 = (-b-raiz_delta)/2
        print('Raíz única.')
        print(f'{x1}')
        
# Soma e produto só podem ser feitos se usar Bhaskara antes.
"""soma = x1 + x2
produto = x1 * x2
sominha = -b/a
produtinho = c/a
if (soma == sominha and produto == produtinho):
    if (x1 in soma == x1 in produto and x2 in soma == x2 in produto):
        print(f'Raízes: {x1}, {x2}')
    else:
        print(f'Não foi possível encontrar raízes.')"""