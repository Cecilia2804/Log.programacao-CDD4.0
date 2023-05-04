#faça um algoritmo que leia a idade de uma pessoa expressa em anos, messes e dias
#e escreva a idade dessa pessoa expressa apenas em dias.
#considrar ano com 365 dias e mes com 30 dias
dias = int(input("digite a idade expressa em dias:"))
meses = int(input("digite a sua idade expressa em meses:"))
anos = int(input("e em anos?"))

anos = anos * 365
meses = meses * 30
soma = anos + meses + dias
print("sua idade é:", soma)



