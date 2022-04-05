# Faça um programa, em linguagem Python, que lê 5 frases, informadas pelo usuário, de, no
# máximo, 50 caracteres cada uma e armazene-as em um arquivo. Mas, antes de gravar cada
# frase no arquivo, é necessário converter todas as suas letras para maiúsculas. O nome do ar-
# quivo será fornecido, via teclado, pelo usuário. A seguir, feche o arquivo. Reabra o arquivo,
# para leitura, exibindo na tela todas as frases convertidas.
# Dica:
# 1. A função que converte minúscula para maiúscula é o upper().
# 2. Como cada texto pode ter tamanho diferente, será necessário gravar antes de cada fra-
# se o tamanho do texto a ser lido. Logo serão necessários dois comandos de gravação e
# leitura (um para o número inteiro que indica a quantidade de caracteres da frase e ou-
# tro para a frase com o tamanho lido).
import numpy as np

frase = np.ones("", str)
# Pega o nome do arquivo
nome_arq = input("Digite o nome do arquivo: ")
# Cria o arquivo texto
arq = open(nome_arq + ".txt", "w")
# Pega a frase
for i in range(5):
    frase = input("Digite a %d frase:" % (i + 1))
    # Deixa a frase em letra maiúscula
    frase = frase.upper()
    # Escreve a frase dentro do arquivo texto
    arq.write(frase + "\n")
# Fecha o arquivo
arq.close()
print("\n")
# Abre o arquivo texto já definido
arq = open(nome_arq + ".txt", "r")
# Lê o que está escrito dentro do arquivo texto
texto = arq.read()
# Imprime na tela o conteúdo lido do arquivo texto
print(texto)
# Fecha o arquivo
arq.close()
