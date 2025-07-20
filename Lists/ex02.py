# Sistema que indica produto mais barato

print("Bem-vindo ao MaisBarato Sys!\nO sistema que te indica onde comprar pelo menor preço!")
print("*"*50)
list = []
preco_1 = float(input("Insira o preço do 1° produto:\n"))
list.append(preco_1)
preco_2 = float(input("Insira o preço do 2° produto:\n"))
list.append(preco_2)
preco_3 = float(input("Insira o preço do 3° produto:\n"))
list.append(preco_3)

print(f'Maior preço: R${max(list)}')
print(f'Menor preço: R${min(list)}')