def VM(a,b):
    velocidade = (a/b)
    return velocidade
try:
    a = int(input("Digite a distancia: "))
    b = int(input("Digite o tempo: "))
    print(VM(a,b))
except:
    print("Digite valores validos")
