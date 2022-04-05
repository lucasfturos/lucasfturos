# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) produto do dobro do primeiro com metade do segundo .
# b) soma do triplo do primeiro com o terceiro.
# c) terceiro elevado ao cubo.
print("\nInforme dois números inteiros e um número real")
num1 = int(input("\nInforme um número inteiro: "))
num2 = int(input("\nInforme outro número inteiro: "))
num3 = float(input("\nInforme um número real: "))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3**3

print("\nProduto do dobro do primeiro com metade do segundo. Resultou em: ", a)
print("\nSoma do triplo do primeiro com o terceiro. Resultou em: {:.2f}".format(b))
print("\nTerceiro elevado ao cubo. Resulto em: {:.2f}".format(c))
