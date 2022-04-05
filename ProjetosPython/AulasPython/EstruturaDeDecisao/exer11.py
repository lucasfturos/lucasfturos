# As Organizações Tabajara resolveram dar um aumento de salário aos seus
# colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte
# critério, baseado no salário atual:
#     salários até R$ 280,00 (incluindo) : aumento de 20%
#     salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#     o salário antes do reajuste;
#     o percentual de aumento aplicado;
#     o valor do aumento;
#     o novo salário, após o aumento.

print("\nPrograma de reajuste salarial")
salario = float(input("Informe seu salário: "))

if salario <= 280.0:
    valor_aumento = salario * (20 / 100)
    result = salario + valor_aumento
    print("Salário antes do ajuste: R$", salario)
    print("Percentual de 20% de aumento")
    print("Valor do aumento: R$%.2f" % valor_aumento)
    print("Novo salário de R$%.2f, após o aumento" % result)
elif salario <= 700.0 and salario > 280:
    valor_aumento = salario * (15 / 100)
    result = salario + valor_aumento
    print("Salário antes do ajuste: R$", salario)
    print("Percentual de 15% de aumento")
    print("Valor do aumento: R$%.2f" % valor_aumento)
    print("Novo salário de R$%.2f, após o aumento" % result)
elif salario <= 1500.0 and salario > 700.0:
    valor_aumento = salario * (10 / 100)
    result = salario + valor_aumento
    print("Salário antes do ajuste: R$", salario)
    print("Percentual de 10% de aumento")
    print("Valor do aumento: R$%.2f" % valor_aumento)
    print("Novo salário de R$%.2f, após o aumento" % result)
else:
    valor_aumento = salario * (5 / 100)
    result = salario + valor_aumento
    print("Salário antes do ajuste: R$", salario)
    print("Percentual de 5% de aumento")
    print("Valor do aumento: R$%.2f" % valor_aumento)
    print("Novo salário de R$%.2f, após o aumento" % result)
