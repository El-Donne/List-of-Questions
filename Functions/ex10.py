# Função que mostra os números pares de uma lista

def evenNumbersList(*x):
    x = list(x)
    evenList = []
    for i in x:
        if i % 2 == 0:
            evenList.append(i)
    print(evenList)
    
evenNumbersList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)