# Pede para digitar quatro pokémons
print('*'*50)
print('CADASTRO DE POKÉMONS')
print('*'*50)

pokemons = []

for i in range(1, 5):
    pokemon_user = input(f'Insira o nome do {i}° pokémon:\n')
    pokemons.append(pokemon_user)

pokemons = tuple(pokemons)
print(pokemons)