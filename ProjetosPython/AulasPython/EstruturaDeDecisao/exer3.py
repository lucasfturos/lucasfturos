# Faça um Programa que verifique se uma letra digitada
# é "F" ou "M". Conforme a letra escrever: F - Feminino,
# M - Masculino, Sexo Inválido.
print("\nInforme seu sexo")
sexo = input("M - Masculino ou F - Feminino:\n")

if "M" == sexo or "Masculino" == sexo or "m" == sexo or "masculino" == sexo:
    print("Masculino")
elif "F" == sexo or "Feminino" == sexo or "f" == sexo or "feminino" == sexo:
    print("Feminino")
else:
    print("Sexo Inválido")
