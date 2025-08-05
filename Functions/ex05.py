# Fatorial de um número

def Fatorial(x):
    cont = x
    while cont > 0:
        fatorial = x * (x-1)
        x -= 1
        cont -=1
    print(fatorial)
    
Fatorial(4)