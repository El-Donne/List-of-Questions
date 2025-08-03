# 5 perguntas sobre um crime;
# 2 questões: suspeito;
# 3-4 questões: cúmplice;
# 5 questões: assassino;
# Nenhuma: livre;

suspect = []

print('*'*50)
print('BEM-VINDO AO SISTEMA DE INVESTIGAÇÃO DE\nSÃO JOÃO DO RIO DO PEIXE - PB')
print('*'*50)
print('FALE SOMENTE A VERDADE!')

question1 = input('Telefonou para a vítima? (S/N)\n')
question2 = input('Esteve no local do crime? (S/N)\n')
question3 = input('Mora perto da vítima? (S/N)\n')
question4 = input('Devia para a vítima? (S/N)\n')
question5 = input('Já trabalhou com a vítima? (S/N)\n')

# Condicionais
if question1 == 's' or question1 == 'S':
    suspect.append(question1)
else:
    pass
if question2 == 's' or question2 == 'S':
    suspect.append(question2)
else:
    pass
if question3 == 's' or question3 == 'S':
    suspect.append(question3)
else:
    pass
if question4 == 's' or question4 == 'S':
    suspect.append(question4)
else:
    pass
if question1 == 's' or question5 == 'S':
    suspect.append(question5)
else:
    pass

tamanhoLista = len(suspect)

if tamanhoLista == 2:
    print('Você foi considerado SUSPEITO')
elif tamanhoLista == 3 or tamanhoLista == 4:
    print('Você foi considerado CÚMPLICE')
elif tamanhoLista == 5:
    print('Você foi considerado ASSASSINO!\nMÃOS PRA CIMA!')
    exit()
else:
    print('Você foi considerado INOCENTE\nLIBERADO, POR ENQUANTO...')