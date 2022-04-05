# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
#     A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#     A mensagem "Reprovado", se a média for menor do que sete;
#     A mensagem "Aprovado com Distinção", se a média for igual a dez.

print("\nCálculo de média do aluno")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("\nInforme a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7.0 and media <= 9.9:
    print("Aprovado. Média do aluno: %.2f\n" % media)
elif media == 10.0:
    print("Aprovado com Distinção. Média do aluno: %.2f\n" % media)
elif media <= 6.9:
    print("Reprovado. Média do aluno: %.2f\n" % media)
