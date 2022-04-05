# Desenvolva um gerador de tabuada, capaz de gerar
# a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja
# ver a tabuada.

n = int(input("\nInforme um número para saber sua tabuada: "))
print("Tabuada do %d" % n)
for i in range(10):
    i += 1
    result = n * i
    print("%d x %d = %d" % (n, i, result))
