# Faça um Programa que leia três números e mostre o maior e o menor deles.

print("\nInforme três número e será mostrado o maior e o menor\n")

n1 = input("Informe o primeiro número: ")
n2 = input("\nInforme o segundo número: ")
n3 = input("\nInforme o terceiro número: ")

if n1 > n2 and n1 > n3:
    print("\nO primeiro número é maior")
elif n2 > n1 and n2 > n3:
    print("\nO segundo número é maior")
elif n3 > n1 and n3 > n2:
    print("\nO terceiro número é maior")
elif n1 < n2 and n1 < n3:
    print("O primeiro número é menor\n")
elif n2 < n1 and n2 < n3:
    print("O segundo número é menor\n")
elif n3 < n1 and n3 < n2:
    print("O terceiro número é menor\n")
else:
    print("Todos são iguais")
