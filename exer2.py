def crescente(a,b,c):
    if a > b and a > c:
        if b > c:
            return c,b,a
        else:
            return b,c,a
    elif b > a and b > c:
        if a > c:
            return c,a,b
        else:
            return a,c,b
    elif c > a and c > b:
        if a > b:
            return b,a,c
        else:
            return a,b,c


a = int(input("Digite o 1o valor: "))
b = int(input("Digite o 2o valor: "))
c = int(input("Digite o 3o valor: "))
print(crescente(a,b,c))
