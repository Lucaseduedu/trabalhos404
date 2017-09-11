def dinheiro(x):
    if x > 20:
        return "va ao cinema"
    else:
        return "fique vendo TV"
try:
    x = int(input("Digite o valor: "))
    print(dinheiro(x))
except:
    print("Digite um valor valido")
