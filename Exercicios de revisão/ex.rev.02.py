#criar um algoritmo que leia um numero difrente de zero
#e diga se o numero é positivo ou negativo

num = int(input("digite um numero diferente de zero: "))
if num < 0:
    print("esse numero é negativo", num)
elif num == 0:
    print("numero ivalido!! digite outro numero difrente de zero")
else:
    print("esse numero é positivo", num)
