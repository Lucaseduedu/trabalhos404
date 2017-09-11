def votar(idade):
    if (2017 - idade) > 18 :
        return  "Voce pode votar"
    elif (2017 - idade) < 18:
        return  "Nao pode votar"
try:
	idade = int(input("Digite sua idade: "))
	print(par(x))
except:
	print("Digite sua idade corretamente")
