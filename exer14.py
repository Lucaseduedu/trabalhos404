def mat(v1,v2):
    if v1 %2 == 0 and v2 %2 == 0:
        return "os dois sao pares"
	elif v1 %2 != o and v2 %2 != 0:
		return "os dois sao impares"
	elif v1 %2 == 0 and v2 %2 != 0:
        return "O primeiro	é	par	e	o	segundo	é	ímpar"
	elif v1 %2 != o and v2 %2 == 0:
		return "O	primeiro	é	ímpar	e	o	segundo	é	par"
try:
	v1 = int(input("Digite o 1o numero: "))
	v2 = int(input("Digite o 2o numero: "))
	print(mat(v1,v2))
except:
	print("Digite apenas numero")