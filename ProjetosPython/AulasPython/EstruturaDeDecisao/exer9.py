# Faça um Programa que leia três números e mostre-os em ordem decrescente.

print("\nInforme três número e será mostrado em ordem decrescente\n")

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("\nInforme o segundo número: "))
n3 = int(input("\nInforme o terceiro número: "))

print("\nPrimeiro %d - Segundo %d - Terceiro %d\n" % (n1, n2, n3))

if n2 > n1:
    aux = n2
    n2 = n1
    n1 = aux
elif n2 > n3:
    aux = n2
    n2 = n3
    n3 = aux
elif n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux

print("\nPrimeiro %d - Segundo %d - Terceiro %d\n" % (n1, n2, n3))
