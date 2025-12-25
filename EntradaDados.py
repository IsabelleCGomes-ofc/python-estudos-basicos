from pythonBasico.TipoVariavel import salario

fruta = input("digite uma fruta: ")
print(fruta)

#obs: tem que converter inputs não strings

codigo = int(input("digite um codigo: "))
nome = input("digite seu nome: ")
salario = float(input("digite seu salario: "))
ativo = True

print("Codigo: %d"% codigo)
print("Nome: %s"% nome)
print("Salario: %.2f"% salario)
print("Ativo: %r"% ativo)

