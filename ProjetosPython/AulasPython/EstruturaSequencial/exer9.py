# Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

print("\nConversor de Fahrenheit para Celsius")
F = float(input("Informe graus Fahrenheit:\n"))

C = 5 * ((F - 32) / 9)

print("De {:.2f}".format(F), "ºF para {:.2f}".format(C), "ºC")
