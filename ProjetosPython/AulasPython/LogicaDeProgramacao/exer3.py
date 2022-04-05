# Dizemos que uma matriz quadrada inteira é um quadrado mágico se a soma dos elementos de
# cada linha, a soma dos elementos de cada coluna e a soma dos elementos das diagonais
# principal e secundária são todas iguais. Dada uma matriz quadrada dimensão MxM, verifique se ela
# é um quadrado mágico através de um algoritmo. Exemplo de matriz quadrado mágico:
# 8  0 7
# 4  5 6
# 3 10 2
import numpy as np

somaDP = 0
somaDS = 0
vddL = 1
vddC = 1
num = int(input("\nDigite a dimensão que tera a matriz: "))
matriz = np.ones((num, num))

for i in range(num):
    for j in range(num):
        matriz[i][j] = int(
            input("Digite os valores da matriz na posição [%d][%d]: " % (i + 1, j + 1))
        )
# Soma Diagonais Primária e Secundária
somaDP = sum(matriz[i][i] for i in range(num))
somaDS = sum(matriz[i][num - i - 1] for i in range(num))
# Soma Linhas
somaL = np.ones(num)
for i in range(num):
    somaL[i] = 0
    for j in range(num):
        somaL[i] = matriz[i][j] + somaL[i]
# Soma Colunas
somaC = np.ones(num)
for j in range(num):
    somaC[j] = 0
    for i in range(num):
        somaC[j] = matriz[i][j] + somaC[j]
# Compara a soma da linha e coluna se são true
for i in range(num):
    if somaL[i] != somaL[i - 1]:
        vddL = 0
        break
    elif somaC[i] != somaC[i - 1]:
        vddC = 0
        break
# Compara todas as somas e mostra o resultado
if vddL and vddC and somaDP == somaDS and somaDP == somaL[0]:
    print("\nQuadrado Magico")
else:
    print("\nNão é Quadrado Magico")
