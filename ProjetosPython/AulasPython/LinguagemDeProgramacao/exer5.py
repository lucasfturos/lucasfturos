# Faça um programa, em linguagem Python, que:
# a) Crie uma struct chamada ponto2d que tenha como atributos os pontos x,y.
# b) Crie duas estruturas do tipo ponto2d chamadas ponto_inicial e ponto_final.
# c) Mostre um menu com as seguintes opções e implemente‐as:
# [1] Digitar os valores do primeiro ponto
# [2] Digitar os valores do segundo ponto
# [3] Mostrar a distância entre os pontos
# [4] Sair
# Dica:
# Distância entre dois pontos (x1,y1)(x2,y2): f = √((x 1 – x 2 )^ 2 + (y 1 – y 2 )^ 2 )
import math as m
from dataclasses import dataclass


@dataclass
class ponto2d:
    x1: float
    x2: float
    y1: float
    y2: float


def Menu():
    print("-------------------------------------------------------\n")
    print("--------------------------MENU-------------------------\n")
    print("-------Digite 1 para informar os valores de X----------\n")
    print("-------Digite 2 para informar os valores de Y----------\n")
    print("-------Digite 3 para ver a distancia entre os pontos---\n")
    print("-------Digite 4 para encerrar o programa---------------\n")
    print("-------------------------------------------------------\n")


p = ponto2d
while True:
    Menu()
    opc = int(input("Digite aqui: "))
    if opc == 1:
        p.x1 = float(input("Informe o x1: "))
        p.x2 = float(input("Informe o x2: "))
    elif opc == 2:
        p.y1 = float(input("Informe o y1: "))
        p.y2 = float(input("Informe o y2: "))
    elif opc == 3:
        result = m.sqrt((p.x1 - p.x2) ** 2 + (p.y1 - p.y2) ** 2)
        print("A Distância entre os dois pontos: %.2f\n" % result)
    elif opc == 4:
        print("ENCERRANDO TAREFA")
        break
    else:
        print("ERRO\nTente Novamente\n\n")
