# Programa coleta o 'kg' do peixe e calcula o excesso.
# O pescador paga R$4,00 por cada quilo em excesso.
# 'excesso' precisa gravar o excesso e 'multa' o valor a pagar.
# Limite estabelecido: 50kg

print("Bem-vindo ao calculador de quilos excedidos!")
quilos_peixe = float(input("Insira o peso do peixe:\n"))
if (quilos_peixe > 50):
    print(f'Peso do peixe: {quilos_peixe}')
    excesso = quilos_peixe - 50
    print(f'Quantidade de quilos excedida: {excesso}kg')
    multa = excesso * 4
    print(f'Multa a ser paga: R${multa}')
    print('''É aplicada uma multa de R$4.00 para cada quilo excedido.''')
else:
    print(f'Peso do peixe: {quilos_peixe}\nNão será preciso pagar multa.')