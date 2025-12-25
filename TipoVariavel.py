codigo = 123
salario = 1500.00
nome = 'Isa'
situacao = True

tipo = type(salario)

print(salario)
print(tipo)

# pra concatenar usar , ou +
print("codigo:", codigo)
print("salario:", salario)
print("nome:", nome)
print("situacao:", situacao)

#quando for + sempre converter var. pra string -> str(nonString)
print("codigo: "  + str(codigo) + " salario: " + str(salario) + " nome: " + nome)
