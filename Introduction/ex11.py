# Pede dois inteiros e um real;
valor_int_1 = int(input("Insira o primeiro valor:\n"))
valor_int_2 = int(input("Insira o segundo valor:\n"))
valor_real_1 = float(input("Insira um valor real:\n"))

# A) Produto do dobro do primeiro com a metade do segundo
print(f'Produto do dobro do 1° pela metade do 2°:\n{(valor_int_1 * 2) * (valor_int_2 / 2)}')
# B) Soma do triplo do primeiro pelo terceiro
print(f'Soma do triplo do primeiro pelo terceiro:\n{(valor_int_1 * 3) + (valor_real_1)}')
# C) Terceiro elevado ao cubo
print(f'Terceiro elevado ao cubo:\n{(valor_real_1**3)}')