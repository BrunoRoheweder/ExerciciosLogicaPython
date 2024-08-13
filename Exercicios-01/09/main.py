# 09. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

grausFah = float(input("Graus em Fahrenheit: "))

celsius = (grausFah - 32) / 1.8

print(f"Temperatura em Celsius: {celsius}")