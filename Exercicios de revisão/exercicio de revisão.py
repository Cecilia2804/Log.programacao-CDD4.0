#receba as duas notas e calcule a media
nota1 = float(input("digite a nota 1:"))
nota2 = float(input("digite a nota 2:"))
media = (nota1 + nota2)/2
if media >= 7:
    print("aprovado", media)
elif media < 7 and media >= 4:
    print("recuperaçao", media)
else:
    print("reprovado", media)
