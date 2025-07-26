print('*'*50)
print('SISTEMA DE CADASTRO DE PERSONAGENS\nJ2R - THE GAME')
print('*'*50)
characters_list = []

while True:
    print('#'*50)
    character_name = input('Insira o nome do personagem:\n')
    characters_list.append(character_name)
    print(f'Último personagem cadastrado: {characters_list[-1]}')
    print(f'Personagens cadastrados: {len(characters_list)}')
    while True:
        # Esse looping vai iniciar após adicionar os personagens na lista.
        print('-'*50)
        decision = input('Continuar cadastro?\nS\tN\n')
        if (decision == 'N' or decision == 'n'):
            print('CADASTRO FINALIZADO!')
            print(f'Personagens cadastrados: {characters_list}')
            exit()
        elif (decision == 'S' or decision == 's'):
            break
            # Como está dentro de um looping interno, precisa ser quebrado para voltar ao looping anterior.
        else:
            print('[INVÁLIDO]\nTENTE NOVAMENTE')