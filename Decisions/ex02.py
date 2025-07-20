# Pedir um valor e mostrar se é positivo ou negativo

value1 = float(input("Insira um número:\n"))
print('*'*50)
if (value1 > 0):
    print(f'O número {value1} é positivo.')
else:
    print(f'O número {value1} é negativo.')