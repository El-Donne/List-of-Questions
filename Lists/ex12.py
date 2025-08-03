# Idade e alturas de 30 alunos;
# Calcular quantos alunos com mais de 13 anos tem altura inferior à média
age = []
heigth = []
sum_heigths = 0
alunos_13 = []

for i in range(1, 6):
    idade = int(input(f'Idade do {i}° aluno: '))
    altura = float(input(f'Altura do {i}° aluno (m): '))
    age.append(idade)
    heigth.append(altura)

# Agora preciso linkar as duas listas SEM USAR DICIONÁRIO
tamanho_altura = len(heigth)
for x in heigth:
    sum_heigths += x
media = sum_heigths/tamanho_altura
print(f'Média de altura: {media}')
# Média de altura definida

"""for y in age:
    if y > 13:
        if heigth[y] < media:
            alunos_13.append(y)"""
            
for i in range(tamanho_altura): # Pega o tamanho da lista
        if age[i] > 13:
            if heigth[i] < media:
                alunos_13.append(age)
                
print(alunos_13)