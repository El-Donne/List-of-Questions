# Ler 10 números reais e mostrá-los em ordem inversa
lista = []
for i in range(1, 11):
    real_numb = float(input(f'Insira o {i}° número:\n'))
    lista.append(real_numb) # Todos os métodos de listas são feitos SEM DECLARAR VARIÁVEL.
    """i += 1""" # O for já faz isso automaticamente
    
"""lista.reverse()
print(lista)"""
# Vai imprimir a lista ao contrário

print(lista[::-1])
# "::-1" indica que queremos um início e fim indefinido (toda a lista);
# ":-1" indica que queremos do início até o último elemento;