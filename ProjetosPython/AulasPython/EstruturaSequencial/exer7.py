# Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.

print("Informe o comprimento do quadrado")
print("para receber o dobro da área do quadrado")
compri = float(input("Informe o comprimento do quadrado:\n"))

area = compri**2
dobro = area * 2
print("A área do quadrado é: {:.2f}".format(area))
print("O dobro da área do quadrado é: {:.2f}".format(dobro))
