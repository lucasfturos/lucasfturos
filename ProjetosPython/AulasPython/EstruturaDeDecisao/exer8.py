# Faça um programa que pergunte o preço de três produtos
# e informe qual produto você deve comprar, sabendo que
# a decisão é sempre pelo mais barato.

print("Informe três produtos e retorna o mais barato")

n1 = input("Informe o primeiro produto: ")
n2 = input("\nInforme o segundo produto: ")
n3 = input("\nInforme o terceiro produto: ")

if n1 < n2 and n1 < n3:
    print("\nO primeiro produto é mais barato\n")
elif n2 < n1 and n2 < n3:
    print("\nO segundo produto é mais barato\n")
elif n3 < n1 and n3 < n2:
    print("\nO terceiro produto é mais barato\n")
elif n1 == n2 and n1 and n1 < n3:
    print("\nO primeiro e segundo produto são mais baratos\n")
elif n1 == n3 and n2 and n3 < n2:
    print("\nO primeiro e o terceiro produto são mais baratos\n")
elif n3 == n2 and n3 and n3 < n1:
    print("\nO segundo e terceito produto são mais baratos\n")
else:
    print("\nTodos são iguais")
