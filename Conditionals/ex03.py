# Entrar numa festa

year_birth = int(input("Em que ano você nasceu?\n"))
age = 2025 - year_birth
if (age >= 18):
    print(f'Idade do usuário: {age}\nBem-vindo à festa!')
else:
    print(f'Idade do usuário: {age}\nVocê é menor de idade e não pode entrar.')