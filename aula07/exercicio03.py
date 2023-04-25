#ler um vetor A de numeros. logo em seguida, ler mais um numero e guardar em uma variavel x
#armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor x. depois, imprimir M

a = []
M = []
for i in range(10):
    a.append(int(input("digite um número: ")))
    x = int(input("digite o  multiplicador: "))
for j in range(10):
    M.append(x*a[j])
print(a)
print(M)
print(x)
