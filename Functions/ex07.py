# Descobrir quantas letras maiúsculas existem dentro de uma string

def Letters():
    x = input('Insira uma frase: ')
    upperLetter = []
    lowerLetter = []
    for i in x:
        if (i.isupper()):
            upperLetter.append(i)
        elif (i.islower()):
            lowerLetter.append(i)
            
    print(f'Frase: {x}')
    print(f'Quantidade de letras maiúsculas: {len(upperLetter)}')
    print(f'Quantidade de letras minúsculas: {len(lowerLetter)}')
    
Letters()