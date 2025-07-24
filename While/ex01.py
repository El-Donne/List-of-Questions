# Pede uma nota entre zero e 10
# Se o valor for inválido, persista
print('*'*50)
print('SISTEMA DE AVALIAÇÃO\nJ2R - THE GAME')
print('*'*50)

while True:
    print('#'*50)
    nota = int(input('Qual nota você dá ao J2R - The Game?\n'))
    if (0 <= nota <= 10):
        if (0 <= nota <=5):
            print(f'Nota {nota}? Que pena...\nVamos melhorar na próxima!')
            exit()
        elif (5 < nota <= 7):
            print(f'Nota {nota}? Razoável!\nIremos continuar nossa melhoria!')
            exit()
        elif (7 < nota <= 10):
            print(f'Nota {nota}?! Show! Não vamos te decepcionar!')
            exit()
    else:
        print('VALOR INVÁLIDO!')