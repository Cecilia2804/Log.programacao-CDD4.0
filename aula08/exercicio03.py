#faça um codigo para ler um valor N qualquer ( que sera o tamanho dos vetores).
#apos, ler dois vetores A e B (de tamanho N cada um)
# e deppois armazenar soma a soma dos elementos do vetor A com os do vetor B
#(respeitando as mesmas posiçoes) e escrever o vetor da soma

a = []
b = []
soma = []
n = int(input("digite um valor de acordo com o tamanho do vetor: "))

for x in range(2):
    a.append(int(input("digite os primeiros valores: ")))
    b.append(int(input("digite os segundos valores: ")))
    soma.append(a[x]+b[x])
print(soma)