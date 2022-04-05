# Uma certa empresa fez uma pesquisa de mercado para saber se as pessoas
# gostaram ou não do seu último produto lançado. Para isto, coletou o sexo do entrevistado
# e a sua resposta (sim ou não). Sabendo que foram entrevistadas 150 pessoas, fazer um
# algoritmo que calcule e mostre ao final:
#   O número de pessoas que responderam sim;
#   O número de pessoas que responderam não;
#   A percentagem de pessoas do sexo feminino que responderam sim;
#   A percentagem de pessoas do sexo masculino que responderam não;
# Para a resposta SIM/NÃO. Utilize uma variável do tipo CHAR, que armazena S ou N,
# ou use uma variável do tipo INT que armazena 1 (para SIM) e 2 (para NÃO).

boole = 0
masc = 0  # num de homens
fem = 0  # num de mulher
sim = 0  # calcula respostas sim
nao = 0  # calcula respostas nao
n = 0  # num de pessoas
res_s_fem = 0  # contador de respostas sim de mulher
res_n_masc = 0  # contador de respostas nao de homem
resp = 0  # contador de respostas

num = int(input("\nDigite o número de entrevistados: "))

while True:
    sexo = input("\nDigite o seu sexo.\nM para masculino F para feminino: ")

    resp = int(
        input(
            "Se o produto lançado agradou o entrevistado\nDigite 1 para Sim ou 0 para Nao: "
        )
    )
    if sexo == "M" or sexo == "m":
        masc += 1
        if resp == 0:
            res_n_masc += 1

    elif sexo == "F" or sexo == "f":
        fem += 1
        if resp == 1:
            res_s_fem += 1

    if resp == 1:
        sim += 1
    elif resp == 0:
        nao += 1

    n += 1
    if n == num:
        break
print("\n\nNúmero de pessoas que responderam Sim:", sim)
print("\nNúmero de pessoas que responderam Não: ", nao)

fs = 100 / (res_s_fem * num)
mn = 100 / (res_n_masc * num)

print("\nPercentual do sexo Masculino que respondeu Não: %.2f" % mn)
print("\nPercentual do sexo Feminino que respondeu Sim: %.2f" % fs)
