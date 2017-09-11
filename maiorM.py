maiorN = 0
aluno = ""
for(1, 11)
nome = input("Digite o nome do aluno")
nota = int(input("Digite a nota do aluno"))
if nota > maiorN:
	maiorN = nota
	aluno = nome
else:
	maiorN = maiorN
print("",aluno,maiorN)
