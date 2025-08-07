# Verificar se uma string é palíndromo

def stringPalyndrome():
    x = input('Insira sua palavra ou frase: ')
    reverse_x = '' # Começar uma string vazia
    for i in x: # Vai percorrer toda a string
        reverse_x += i[::-1]
        
    for j in range(len(x)):
        if x[j] == reverse_x[j]:
            pass
        
            
stringPalyndrome()