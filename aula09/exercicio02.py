#crie um algoritmo que leia um numero diferente de zero e diga se este numero é positivo ou negativo
continuar = "sim"
while continuar == "sim":
    num = float(input("digite um numero: "))
    if num == 0:
        print("invalido, digite outro numero difrente de 0")
    elif num < 0:
        print("numero negativo")
    else:
        print("numero positivo")
    continuar = (input("deseja continuar?"))
