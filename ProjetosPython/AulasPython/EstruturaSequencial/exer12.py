# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

print("Calculadora de peso ideal pela altura")
altura = float(input("\nInforme sua altura em metros: "))

peso = (72.7 * altura) - 58

print("\nPeso ideal para a altura {:.2f} m".format(altura), " é {:.2f} kg".format(peso))
