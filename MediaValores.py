qnt = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

#soma positivos
if valor > 0 :
    while valor > 0.0:
        soma += valor
        qnt += 1
        valor = float(input("Digite um valor: "))
    media = soma / qnt

#encerra quando valor é negativo
print("\n Total da soma:", soma)
print("\n Quantidade de valores digitados:", qnt)
print("\n Média dos valores:", media)