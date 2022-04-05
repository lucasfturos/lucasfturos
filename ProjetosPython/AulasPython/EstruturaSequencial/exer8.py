# Faça um Programa que pergunte quanto você ganha
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salario_h = float(input("Informe qual seu salário por \nhora trabalhada:\n"))
num_hora = float(input("\nInforme o número de horas trabalhadas no mês:\n"))

total_trabalhado = salario_h * num_hora

print("\nTotal do seu salário no referido mês: {:.2f}".format(total_trabalhado))
