# Para cada um dos consumidores de energia elétrica de uma cidade é informado o número da
# conta e o total de KW consumido no mês. Sabendo-se que o custo do KW é de R$ 1,75, fazer
# um algoritmo para:
#   Armazenar e listar o número da conta, o total de KW consumidos e o valor a pagar de
# cada consumir cadastrado
#   Listar o número da conta, o total de KW consumidos e o valor a pagar do consumidor
# que mais gastou e o que menos gastou
#   Mostrar a média de consumo da cidade
#   Mostrar o número de consumidores que ultrapassaram o consumo de 170 KW
# Armazene as informações em estruturas de vetores e/ou matrizes. Na tela, deve existir um
# MENU que pergunta ao usuário se ele deseja cadastrar um novo consumidor ou listar alguma
# informação (maior, menor, média, etc.).
import os
import numpy as arr

numconsu = arr.array(float)
numconta = arr.array(int)
valorpagar = arr.array(float)
totalconsu = arr.array(float)


def menuPrincipal():
    os.system("cls || clear")
    print("\n|-----------------------------------------------|\n")
    print("|-----------------------------------------------|\n")
    print("|---------- 1 CADASTRO DO CLIENTE --------------|\n")
    print("|-----------------------------------------------|\n")
    print("|-----------------------------------------------|\n")
    print("|---------- 2 LISTAR INFORMACAO ----------------|\n")
    print("|-----------------------------------------------|\n")
    print("|-----------------------------------------------|\n")
    print("|---------- 3 SAIR DO PROGRAMA -----------------|\n")
    print("|-----------------------------------------------|\n")
    print("|-----------------------------------------------|\n\n")


while True:
    menuPrincipal()
    case = int(input("Informe a opção do menu: "))
    if case == 1:
        # os.system("cls || clear")
        num = int(input("\nInforme quantas pessoas vai cadastrar: "))
        for i in range(num):
            numconta = arr.array(float(input("\nInforme o número da conta: ")))
            totalconsu = arr.array(
                float(input("\nInforme o total de KW consumidos do mês: "))
            )
            valorpagar = arr.array(1.75 * totalconsu)
            if totalconsu > 170:
                numconsu = arr.array(i + 1)

    elif case == 2:
        for i in range(num):
            print("O numero da conta eh: \n%d" % numconta)
            print("O total de KW consumidos eh: \n%.2f" % totalconsu)
            print("O valor total a pagar eh: \n%.2f" % valorpagar)

            if totalconsu > 170.0:
                print("Consumiu mais que 170 KW\n")
            else:
                print("Consumiu menos que 170 KW\n")
        print(
            "Numero de consumidores que ultrapasssaram\no consumo de 170 KW: ",
            numconsu,
        )
        print(
            "\n\nMedia de consumo da cidade: \n",
            (float(valorpagar) / float(numconsu)),
        )

        opc = int(input("\nDeseja continuar no sistema?\nSe sim (1), se não (0): "))
        if 0 == opc:
            break

    elif case == 3:
        # os.system("cls || clear")
        break
    else:
        print("ERRO")
