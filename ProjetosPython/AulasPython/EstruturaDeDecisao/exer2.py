# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print("\nRecebe um número positivo ou negativo")

num = int(input("Informe um número positivo ou negativo: "))

if num > 0:
    print("Número %d é positivo" % num)
else:
    print("Número %d é negativo" % num)
