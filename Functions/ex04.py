"""# Printar uma frase ao contrário

def ReverseString(x):
    word = []
    for i in x:
        word.append(i)
    word.reverse()
    print(word)
    
ReverseString("Olá! Bom dia!")"""

# Versão 2

def ReverseTwo(x):
    reverse_x = '' # Precisa iniciar vazia
    length = len(x)
    # Dá para descobrir tamanho da palavra usando o 'len()'
    while length > 0:
        reverse_x += x[length-1]
        length -= 1
        # Vai fazer isso até chegar em 0
        
    print(reverse_x)
    
ReverseTwo('Olá, mundo!')

# Versão 3

def ReverseThree(y):
    print(y[::-1])
    
ReverseThree('Opa!')