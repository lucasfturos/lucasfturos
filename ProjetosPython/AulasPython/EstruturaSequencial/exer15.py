# Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a) salário bruto.
# b) quanto pagou ao INSS.
# c) quanto pagou ao sindicato.
# d) o salário líquido.
# e) calcule os descontos e o salário líquido, conforme a tabela abaixo:
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$
#     Obs.: Salário Bruto - Descontos = Salário Líquido.
print("\nCalculadora de desconto do Salário")
salario_h = float(input("Informe seu salário por hora trabalhada:"))
hora = float(input("Informe as horas trabalhadas no mês: "))

salario_bruto = salario_h * hora
ir = (11 / 100) * salario_bruto
inss = (8 / 100) * salario_bruto
sindicato = (5 / 100) * salario_bruto
desconto = ir + inss + sindicato
salario_liquido = salario_bruto - desconto

print("\nTabela de descontos")
print("Salário Bruto: R${:.2f}".format(salario_bruto))
print("IR (11%): R${:.2f}".format(ir))
print("INSS (8%): R${:.2f}".format(inss))
print("Sindicato (5%): R${:.2f}".format(sindicato))
print("Salário Liquido: R${:.2f}".format(salario_liquido))
