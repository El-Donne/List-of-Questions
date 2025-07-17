# Pedir quatro notas e imprimir a média

# Versão 1
nota1 = float(input("Insira a 1° nota:\n"))
nota2 = float(input("Insira a 2° nota:\n"))
nota3 = float(input("Insira a 3° nota:\n"))
nota4 = float(input("Insira a 4° nota:\n"))

print("A média aritmética das notas é: ", nota1 + nota2 + nota3 + nota4 / 4) 
# Interpreta que quero dividir somente a 4° nota.
print("A média aritmética das notas é: ", (nota1 + nota2 + nota3 + nota4)/4)
# O parênteses serve para colocar a operação dentro de um conjunto.

# Versão 2
media = (nota1 + nota2 + nota3 + nota4) / 4
# O cálculo será armazenado em uma variável.
print(f"Média aritmética das notas: {media}")