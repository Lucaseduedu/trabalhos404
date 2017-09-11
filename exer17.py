def indice(peso,altura):
    imc = peso/(altura * altura)
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obeso leve"
    elif imc < 40:
         return "Obeso moderado"
    elif imc >= 40:
         return "Obeso morbido"
try:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    print(indice(peso,altura))
except:
    print("Digite valores validos")