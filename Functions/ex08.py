# Retorna uma lista sem duplicadas

def noDuplicates(*x):
    x = set(x)
    x = list(x)
    print(f'Duplicadas removidas!\n{x}')
    
noDuplicates(1, 2, 2, 3, 3, 3, 4, 5, 5, 6)