# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print("Informe as 4 notas bimestrais")
nota1 = int(input("Informe a primeira nota: "))
nota2 = int(input("Informe a segunda nota: "))
nota3 = int(input("Informe a terceira nota: "))
nota4 = int(input("Informe a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4

print("A média das 4 notas: ", media)
