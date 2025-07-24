# Pede usuário e senha
# Se a senha for igual ao usuário, pede de novo

print('*'*50)
print('SISTEMA DE PRÉ-VENDA\nJ2R - THE GAME')
print('*'*50)

print('Bem-vindo à pré-venda do J2R - The Game!\nPor favor, preencha as informações abaixo!')
while True:
    username = input('Nome de usuário: ')
    password = input('Senha: ')
    if (username != password):
        print('Obrigado pelo cadastro!')
        exit()
    elif (username == password):
        print('Usuário e senha precisam ser DIFERENTES!\nInsira as informações novamente.')