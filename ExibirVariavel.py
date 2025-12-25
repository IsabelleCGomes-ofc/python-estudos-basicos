#mascara de formatação: como exibe um número em formato texto, legível e bonito
# dicionário, exibe:%d/%i - int; %f - float/double(decimal); %ld - longInt;%e/%E - exponecial;
#[...]%c - char; %o - intOctal(0 a 7); %x/%X - intHexa(0 a F); %s - string;%r - booleano;

codigo = 123
nome = 'Isabelle'
salario = 1600.00
ativo = True

print("Codigo: %d"% codigo)
print("Nome: %s"% nome)
print("Salario: %.2f"% salario) # ".2" casas exibidas após o ".";
print("Ativo: %r"% ativo)