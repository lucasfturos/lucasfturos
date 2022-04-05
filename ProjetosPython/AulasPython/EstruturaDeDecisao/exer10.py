# Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

print("\nInforme em qual turno você estuda")
turno = input("M-matutino ou V-Vespertino ou N- Noturno\nInforme aqui: ")

if "m" == turno or "M" == turno or "matutino" == turno or "Matutino" == turno:
    print("\nBom dia\n")
elif "v" == turno or "V" == turno or "vespertino" == turno or "Vespertino" == turno:
    print("\nBoa Tarde")
elif "n" == turno or "N" == turno or "noturno" == turno or "Noturno" == turno:
    print("\nBoa Noite\n")
else:
    print("\nValor Inválido")
