# Converte a tupla em um set caso esteja com ITENS DUPLICADOS

listaPokemons = ['Charmander', 'Pikachu', 'Squirtle', 'Bulbasaur', 'Mewtwo', 'Gato da Rocket']
time = []

while True:
    cadastro = input('Escolha o seu time:\n')
    if cadastro in listaPokemons:
        time.append(cadastro)
        decisao = int(input('Deseja continuar?\n1 - S\t2 - N\n'))
        if decisao == 1:
            continue
        elif decisao == 2:
            break
    
# Verificar se a lista têm duplicadas
print('#'*50)
print('Verificar se a lista têm duplicadas')
print('#'*50)
while True:
    itemVerificar = input('Insira o Pokémon a verificar:\n')
    contarPokemon = time.count(itemVerificar)
    if contarPokemon > 1:
        print('ITEM DUPLICADO!')
        time = set(time)
        time = tuple(time)
    else:
        time = tuple(time)
    decisao = int(input('Deseja continuar?\n1 - S\t2 - N\n'))
    if decisao == 1:
        continue
    elif decisao == 2:
        break
    
print(time)