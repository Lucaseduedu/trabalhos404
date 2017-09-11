def est(temp):
    if temp > 36.5:
        return "esta com febre"
	elif temp =< 36.5:
		return "sem febre"
try:
	temp = int(input("Digite sua temperatura: "))
	print(est(temp))
except:
	print("Digite uma temperatura valida")