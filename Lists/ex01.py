# Ler três números e ler o maior deles
list1 = [] # Armazenará os valores

value1 = float(input("Insira o 1° número:\n"))
list1.append(value1)
value2 = float(input("Insira o 2° número:\n"))
list1.append(value2)
value3 = float(input("Insira o 3° número:\n"))
list1.append(value3)

print(f'Maior número: {max(list1)}')
print(f'Menor número: {min(list1)}')