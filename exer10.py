def mat(x):
    if x%2 == 0 and x%3 == 0:
        return  True
    else:
        return  False
try:
	x = int(input("Digite um valor: "))
	print(mat(x))
except:
	print("Digite um numero inteiro")