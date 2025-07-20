# Leitura de notas parciais de um aluno.
# Calcula a média e retorna sua situação

print("Bem-vindo ao Sistema de Notas da Faculdade Católica da Paraíba")
print("*"*50)
nota1 = int(input("Insira a 1° nota:\n"))
nota2 = int(input("Insira a 2° nota:\n"))
nota3 = int(input("Insira a 3° nota:\n"))
nota4 = int(input("Insira a 4° nota:\n"))
media = (nota1 + nota2 + nota3 + nota4) / 4

if (media >= 70):
    print(f"Média:{int(media)}\nAluno aprovado.")
    if (media == 100):
        print(f"Média:{int(media)}\nALUNO APROVADO COM DISTINÇÃO.")
else:
    print(f"Média:{int(media)}\nReprovado.")