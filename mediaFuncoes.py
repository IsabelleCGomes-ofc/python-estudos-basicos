def lerNotas():
    nota = float(input("Digite a nota do aluno: "))
    return nota


def calculoMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    print("Nota 1: %.2f" % nota1)
    print("Nota 2: %.2f"% nota2)
    print("Media: %.2f" % media, " Resultado: ", end='')
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
#end é o que define o que acontece no fim da linha, com relação ao próximo print ex:se
#coloco \n o próximo print vai pra linha de baixo, no caso desse end, o print vai ao lado


nota1 = lerNotas()
nota2 = lerNotas()
calculoMedia(nota1, nota2)
