alunos = {} #array assoc vazio

aluno = { #array com 3 dados
    "nome" : "Samuel",
    "rm" : "12345",
    "notas": [7.5, 8.0, 5.0] #dado que recebe array de lista
}

print("Nome: ", aluno["nome"])
print("RM: " , aluno["rm"])
#exibir lista toda: print("Notas: ", aluno["notas"])
#exibir nota por nota
for i, nota in enumerate(aluno["notas"], start=1): #i=contador nota=dado de notas do aluno
    print(f"nota {i}: ", nota)

aluno["nome"] = "Isa" #altera dado
aluno["curso"] = "adm" #cria dado e atributo

for chave, valor in aluno.items():#pega atributo e dado, de todos os items de aluno
    print(chave, ": ",  valor) #exibe ex. "nome(chave): Isa(valor)"

#coloco array assoc dentro de outro
alunos[aluno["rm"]] = aluno
#guardar UM aluno específico em alunos
alunos["12345"] = aluno

#com lista

listaAlunos = []
listaAlunos.append(aluno)
for aluno in listaAlunos:
    print("Nome:", aluno["nome"])
    print("RM:", aluno["rm"])
    for nota in aluno["notas"]:
        print("Nota: ", nota)