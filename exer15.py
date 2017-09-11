def mult(v1,v2,v3):
    if v1 > v2 and v1 > v3:
        return "v1"
	elif v2 > v1 and v2 > v3:
        return "v2	"
	elif v3 > v1 and v3 > v2:
        return "v3"
try:
	v1 = int(input("Digite o 3o numero: "))
	v2 = int(input("Digite o 2o numero: "))
	v3 = int(input("Digite o 3o numero: "))
	print(mat(v1,v2,v3))
except:
	print("Digite apenas numeros")