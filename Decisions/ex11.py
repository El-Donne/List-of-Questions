# Informar um ano e verificar se ele é bissexto
print('*'*50)
print('VERIFICADOR DE ANO BISSEXTO')
print('*'*50)
year = int(input("Insira o ano:\n"))

if (year % 4 == 0 or year % 400 == 0 and year % 100 != 0):
    print('Ano bissexto!')
else:
    print('Ano normal!')