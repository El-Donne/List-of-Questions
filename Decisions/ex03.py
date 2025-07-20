# Verificar qual o sexo da pessoa
print('Bem-vindo ao cadastro do J2R - The Game!')
print("*"*50)
name_j2r = input("Insira um nome de usuário:\n")
email_j2r = input("Insira um e-mail válido\n")
country_j2r = input("Insira o seu país de origem:\n")
sex_j2r = input("Insira o seu sexo:\nMasculino\tFeminino\nEscolha 'M' para Masculino e 'F' para Feminino.\n")
    
print("Dados do usuário")
print(name_j2r)
print(email_j2r)
print(country_j2r)
if (sex_j2r == "M"):
    print("Masculino")
elif (sex_j2r == "F"):
    print("Femino")
else:
    print("[ERRO]\nSEXO NÃO CADASTRADO NO BANCO DE DADOS")