# Pede a temperatura em Celsius e converte para Fahrenheit

# Versão 1
temp_fahrenheit = float(input("Insira a temperatura:\n"))
print(f"Celsius: {temp_fahrenheit}\nFahrenheit: {5 * (temp_fahrenheit - 32) / 9}")

# Versão 2
calculo = 5 * (temp_fahrenheit - 32) / 9
print(f"Celsius: {temp_fahrenheit}°C\nFahrenheit: {calculo}°F")
