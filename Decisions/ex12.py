# Pedir dinheiro no caixa eletrônico
# Mínimo 10, máximo 600
# Notas de 5, 10, 20, 50, 100, 200

print('*'*50)
print('SISTEMA DE SAQUE DO BANCO DO BRASIL')
print('*'*50)
money = int(input("Insira o valor que deseja sacar:\n"))

if (money < 10 or money > 600):
    print('Valor inválido!')
else:
    # Dá para ir desmembrando os valores em R$
    if (money >= 300):
        notas_200 = money // 200 # Preciso começar por debaixo
        money = money - (notas_200 * 200)
        notas_100 = money // 100
        money = money - (notas_100 * 100)
        notas_50 = money // 50
        money = money - (notas_50 * 50)
        notas_20 = money // 20
        money = money - (notas_20 * 20)
        notas_10 = money // 10
        money = money - (notas_10 * 10)
        notas_5 = money // 5
        money = money - (notas_5 * 5)
        
        print(f'{notas_200} nota(s) de R$200')
        print(f'{notas_100} nota(s) de R$100')
        print(f'{notas_50} nota(s) de R$50')
        print(f'{notas_20} nota(s) de R$50')
        print(f'{notas_10} nota(s) de R$10')
        print(f'{notas_5} nota(s) de R$5')
            
    elif (money <=299):
        notas_200 = money // 200 # Preciso começar por debaixo
        money = money - (notas_200 * 200)
        notas_50 = money // 50
        money = money - (notas_50 * 50)
        notas_20 = money // 20
        money = money - (notas_20 * 20)
        notas_10 = money // 10
        money = money - (notas_10 * 10)
        notas_5 = money // 5
        money = money - (notas_5 * 5)
        
        print(f'{notas_200} nota(s) de R$200')
        print(f'{notas_50} nota(s) de R$50')
        print(f'{notas_20} nota(s) de R$50')
        print(f'{notas_10} nota(s) de R$10')
        print(f'{notas_5} nota(s) de R$5')