def numero(x):
    if x > 0:
       return "positivo"
    elif x < 0:
       return "negativo"
    elif x == 0:
        return "igual a 0"
try:
    x = int(input("Digite um valor: "))
    print(numero(x))
except:
    print("Digite um numero")




