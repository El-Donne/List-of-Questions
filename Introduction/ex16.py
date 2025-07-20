# Pedir o tamanho do arquivo em MB e velocidade do link de internet em Mbps.
# Calcular o tempo aproximado do download do linl

tamanho_arquivo = float(input("Insira aqui o tamanho do arquivo:\n"))
print(f'Tamanho do arquivo: {tamanho_arquivo}MB.')
print('*'*50)
velocidade_link = float(input("Insira aqui a velocidade do link:\n"))
print(f'Velocidade do link: {velocidade_link}Mbps.')
print('*'*50)
tempo_segundo = tamanho_arquivo / velocidade_link

# Para converter o tempo em minuto e hora

if (tempo_segundo >= 3600):
    hora = int(tempo_segundo / 3600)
    if (hora == 1):
        print(f'Tempo estimado para finalizar operação: {hora} hora.')
    else:
        print(f'Tempo estimado para finalizar operação: {hora} horas.')
elif (tempo_segundo >= 60):
    minuto = int(tempo_segundo / 60)
    if (minuto == 1):
        print(f'Tempo estimado para finalizar operação: {minuto} minuto.')
    else:
        print(f'Tempo estimado para finalizar operação: {minuto} minutos.')
else:
    print(f'Tempo estimado para finalizar operação: {tempo_segundo}s')