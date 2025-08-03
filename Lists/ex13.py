# Recebe a temperatura média de cada mês;
# Mostra as temperaturas acima da anual e em qual mês ocorreram;

temp_media = []
temps_count = 0

for i in range(1, 13):
    temp = float(input(f'Temperatura do {i}° mês em °C: '))
    temp_media.append(temp)
    temps_count += temp
    
tamanho_lista = len(temp_media)
media_anual = temps_count/tamanho_lista

for x in range(tamanho_lista):
    if temp_media[x] > media_anual:
        """print(f'Temperatura média: {temp_media[x]} -- Mês: {x}')"""
        print(f'Temperatura média: {temp_media[x]}')
        if (x == 1):
            print(f'Mês: 1 - Janeiro.')
        elif (x == 2):
            print(f'Mês: 2 - Fevereiro.')
        elif (x == 3):
            print(f'Mês: 3 - Março.')
        elif (x == 4):
            print(f'Mês: 4 - Abril.')
        elif (x == 5):
            print(f'Mês: 5 - Maio.')
        elif (x == 6):
            print(f'Mês: 6 - Junho.')
        elif (x == 7):
            print(f'Mês: 7 - Julho.')
        elif (x == 8):
            print(f'Mês: 8 - Agosto.')
        elif (x == 9):
            print(f'Mês: 9 - Setembro.')
        elif (x == 10):
            print(f'Mês: 10 - Outubro.')
        elif (x == 11):
            print(f'Mês: 11 - Novembro.')
        elif (x == 12):
            print(f'Mês: 12 - Dezembro.')