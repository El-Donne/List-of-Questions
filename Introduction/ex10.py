# Pede temperatura em Fahrenheit e converte para Celsius
# F to C: 5*(F-32)/9
# C to F: 9*(C+32)/5

# Versão 1
temp_celsius = float(input("Insira a temperatura:\n"))
print(f"Temperatura informada: {temp_celsius}°F")
print(f"Temperatura convertida para Celsius: {(temp_celsius + 32) * 1.8}°C")
print("Fim do programa.")