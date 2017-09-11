def pronome(sexo):
    if sexo  == "m":
        return "Sr"
    elif sexo == "f":
        return "Sra"
nome = str(input("Qual seu nome: "))
sexo = input("Qual seu sexo: ")
print(pronome(sexo))
