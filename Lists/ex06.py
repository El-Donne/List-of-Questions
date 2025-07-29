# Pede um vetor de 10 caracteres
# Quantas consoantes foram lidas

lista = []
tamanho = []
vetor = input('Insira um texto: ')
# Definir o tamanho da lista em 10

for i in vetor:
    tamanho.append(i)

if (len(tamanho) <= 10):
    for x in tamanho:
        if (x!= 'a' and x!= 'e' and x!= 'i' and x!= 'o' and x!= 'u'):
            lista.append(x)
    print(f'A palavra {vetor} possui {len(lista)} consoantes')
else:
    print('TAMANHO EXCEDIDO!\nLimite de até 10 caracteres')