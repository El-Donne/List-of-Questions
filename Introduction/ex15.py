# Pedir o tamanho em 'm²' da área desejada;
# Cobertura de 1L para cada 6m²
# Tinta vendida em latas de 18 litros de R$80.00;
# Galões de 3.6L por R$25.00

print("*"*50)
print("Bem vindo ao sistema de vendas de tintas da Tintas Irmãos Oliveira!")
print("*"*50)

area_desejada = int(input("Insira a área que você deseja pintar:\n"))
print(f'Área escolhida pelo cliente: {area_desejada}m²')
print("Temos a cobertura de 1L para cada 6m².")
cobertura = area_desejada / 6

print(f'Cobertura de {int(cobertura)}L para {area_desejada}m²')
print("Temos 3 opções para você:")
opcoes = input('Latas de 18L - R$80.00\nGalões de 3.6L - R$25.00\nMistura')
latas_18L = 80
galoes_36L = 25

"""if (opcoes == 'Latas de 18L' or 'latas' or 'Latas' or '1°'):
    if ()"""