# Faça um Programa que peça a temperatura
# em graus Celsius, transforme e mostre em graus Fahrenheit.

print("\nConversor de Celsius para Fahrenheit")
C = float(input("Informe graus Celsius:\n"))

F = (C * (9 / 5)) + 32

print("De {:.2f}".format(C), "ºC para {:.2f}".format(F), "ºF")
