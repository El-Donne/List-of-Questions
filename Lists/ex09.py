# Idade e altura de 5 pessoas
# Armazenar com o respectivo vetor
# Imprimir idade e altura em ordem inversa
"""heigth_list = []
age_list = []

for i in range(1, 6):
    heigth = int(input(f'Insira a altura da {i}° pessoa: '))
    heigth_list.append(heigth)
    age = int(input(f'Insira a idade da {i}° pessoa: '))
    age_list.append(age)
print(f'Lista de alturas (invertida): {heigth_list[::-1]}\n \
    Lista de idades (invetida): {age_list[::-1]}')"""

# Usando dicionários
informacoes = {'Altura': [], 'Idade': []}
for x in range(1, 6):
    altura = int(input(f'Insira a algura da {x}° pessoa: '))
    idade = int(input(f'Insira a idade da {x}° pessoa: '))
    informacoes['Altura'].append(altura)
    informacoes['Idade'].append(idade)
    
print(f'Alturas (invetido): {informacoes["Altura"][::-1]}\n \
    Idades (invertido): {informacoes["Idade"][::-1]}')