# Pokémons do tipo Água e Planta
# Sets com tipos dos Pokemóns

userName = input('Insira seu nome de usuário:\n')

print('*'*50)
print(f'POKÉMONS DO {userName}')
print('*'*50)

pokemons_tipos = {'Água', 'Elétrico', 'Planta', 'Fogo'}

while True:
    tiposDesejados = input('Qual o tipo de pokémon você procura?\n')
    if tiposDesejados in pokemons_tipos:
        print(f'Tipo {tiposDesejados} em estoque!')
        decisao = int(input('Deseja continuar?\n1 - S\t2 - N\n'))
        if decisao == 1:
            print('PROGRAMA EM CONSTRUÇÃO')
            exit()
        elif decisao == 2:
            print('PROGRAMA FINALIZADO')
            break
    elif tiposDesejados not in pokemons_tipos:
        print(f'Tipo {tiposDesejados} em falta!')
        cadastro = int(input('Deseja cadastrar?\n1 - S\t2 - N\n'))
        if cadastro == 1:
            pokemons_tipos.add(tiposDesejados)
            print(f'{tiposDesejados} CADASTRADO COM SUCESSO!')
            continue
        elif cadastro == 2:
            break
    else:
        print('[ERRO DESCONHECIDO]')