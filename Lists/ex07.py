# Lê 20 números inteiros e armazena-os em um vetor.
# Vetor par & ímpar
vectors = []
even_vector = []
odd_vector = []

for i in range(1, 21):
    vector_integer = int(input(f'Insira o {i}° número: '))
    vectors.append(vector_integer)
    if (vector_integer % 2 == 0):
        even_vector.append(vector_integer)
    else:
        odd_vector.append(vector_integer)

print(f'Inteiros: {vectors}\n \
    Números pares: {odd_vector}\n \
    Números ímpares: {even_vector}')