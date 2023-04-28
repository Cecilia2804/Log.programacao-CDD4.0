#faça um codigo para ler um vetor de 30 numeros
#apos isso, ler mais um numero qualquer, calcular e escrever quantas vezes esse numero aparece no vetor

n = []
cont = 0
for x in range(4):
    n.append(input("digite um numero: "))
num = float(input("adicione um numero: "))
for y in range(4):
    if num == n[y]:
        cont +=1
print(cont)
