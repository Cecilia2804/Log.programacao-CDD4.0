#crie um algoritmo que receba 3 numeros e informe qual o maior entre eles

n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))
n3 = float(input("digite o terceiro numero:"))
if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)