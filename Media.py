NotaA= float(input("Digite a primeira nota: "))
NotaB= float(input("Digite a segunda nota: "))

#Calcular média
Media= (NotaA+NotaB)/2

#verificação
if Media >= 7:
    print("Media final: %.2f - Aprovado" % Media)
else:
    print("Media final: %.2f - Reprovado" % Media)