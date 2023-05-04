#crie um algoritmo que receba 3 numeros e informe qual o maior entre eles
a = int(input("selecione um numero:"))
b = int(input("selecione um segundo numero:"))
c = int(input("selecione um terceiro numero:"))
if a > b and a > c:
    print(a, "é maior do que", b, "e", c)
elif b > a and b > c:
    print(b, "é maior do que", a, "e", c)
else:
    print(c, "é maior do que", a, "e", b)

