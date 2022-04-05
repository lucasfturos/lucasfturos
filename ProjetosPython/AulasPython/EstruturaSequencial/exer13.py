# Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# a) Para homens: (72.7*h) - 58
# b) Para mulheres: (62.1*h) - 44.7

print("\nCalculadora de peso ideal pela altura para homens e mulheres")
alturaH = float(input("\nInforme a altura em metros do homem: "))

pesoH = (72.7 * alturaH) - 58

print(
    "\nPeso ideal do homem com altura de {:.2f} m".format(alturaH),
    "é {:.2f} kg".format(pesoH),
)

alturaM = float(input("\nInforme a altura em metros da mulher: "))

pesoM = (62.1 * alturaM) - 44.7

print(
    "\nPeso ideal da mulher com altura de {:.2f} m".format(alturaM),
    "é {:.2f} kg\n".format(pesoM),
)
