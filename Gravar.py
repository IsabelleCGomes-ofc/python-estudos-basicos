arquivo = open("arqText.txt", "w")

arquivo.write("Curso Python \n")
arquivo.write("Aula Prática")
arquivo.close()

#ler arquivo
ler = open("arqText.txt", "r")

print(ler.readline())
ler.close()

#parametros de arquivo texto:
#r+ - arquivo precisa existir. Lê e escreve, se houver coisa escrita ele reescreve elas +
# linhas novas
#w+ - lê e escreve. Apaga o que já tinha escrito.
#a - escreve a partir da última linha do txt
#a+ escreve partir da última linha e lê