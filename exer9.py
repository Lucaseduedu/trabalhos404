def mult(valor):
    if temp %7 == 0:
        return "multiplo de 7"
	elif temp =< 36.5:
		return "nao eh multiplo de 7"
try:
	valor = int(input("Digite um numero: "))
	print(mult(valor))
except:
	print("Digite um numero inteiro")