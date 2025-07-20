# Imprimir três números em forma decrescente

list = []

num1 = float(input("insira o 1° número: "))
list.append(num1)
num2 = float(input("insira o 2° número: "))
list.append(num2)
num3 = float(input("insira o 3° número: "))
list.append(num3)

print(list)
list.sort(reverse = True)
# Vai imprimir a lista em ordem decrescente.
print(list)
# Primeiro precisamos definir a função para depois imprimir.