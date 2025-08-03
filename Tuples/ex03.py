# Trocar pokémons exclusivos

mySet = {'Pikachu', 'Bulbasaur', 'Squirtle'}
friendSet = {'Pikachu', 'Charmander', 'Eevee'}

for i in friendSet:
    for x in mySet:
        if i not in mySet:
            switch = input(f'Por qual pokémon você deseja trocar?\n{mySet}\n')
            if switch in mySet:
                mySet.add(i)
                mySet.remove(switch)
                friendSet.remove(i)
                friendSet.add(switch)
        else:
            pass
            
print(f'Seus pokémons: {mySet}')
print(f'Pokémons do amigo: {friendSet}')