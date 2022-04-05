# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
print("\nVerifica se a letra é vogal ou consoante")
letra = input("Informe uma letra: ")

if (
    "a" == letra
    or "e" == letra
    or "i" == letra
    or "o" == letra
    or "u" == letra
    or "A" == letra
    or "E" == letra
    or "I" == letra
    or "O" == letra
    or "U" == letra
):
    print("Vogal\n")
else:
    print("Consoante\n")
