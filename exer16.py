def transt(cor):
    if cor == "V":
        return "Siga"
	elif cor == "A":
		return "Atencao"
	elif cor == "R":
		return "Pare"
try:
	cor = input("Digite uma cor: ")
	print(transt(valor))
except:
	print("Cor invalida")