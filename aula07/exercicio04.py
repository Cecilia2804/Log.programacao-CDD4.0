#faça um codigo para ler 5 numeros e armazenar em um vetor. após a leitura total dos 5 numeros,
#o codigo deve escrever esses 5 numeros lidos na ordem inversa.

numero = []

for x in range(5):
    numero.append(int(input("digite um numero: ")))

for y in range(4, -1, -1):
    print(numero, [y])

    #########
for z in range(5):
    print(numero[4 - z])
