#faça um algoritmo que receba 2 notas e calcule a media aritimetica
# reprovado, aprovado ou recuperaçao

continuar = "sim"
resultado = []
while continuar == "sim":

    nota1 = float(input("digite sua primeira nota:"))
    nota2 = float(input("digite sua segunda nota:"))
    media = (nota1 + nota2) / 2
    resultado.append(media)
    if media >= 7:
        print("sua media é", media, "voce esta em aprovado!")
    elif media >= 4:
        print("sua media foi", media, "voce esta recuperação!")
    else:
        print("voce esta REPROVADO!")
    continuar = input("deseja continuar?")
print(resultado)