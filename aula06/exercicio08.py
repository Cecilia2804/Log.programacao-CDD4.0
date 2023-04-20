#mostrar o nome do aluno e a posição em que ele está
alunos= []
n = int(input("quantos alunos tem na sala? "))
for x in range(n):
    nomes = input("digite o nome do aluno: ")
    alunos.append(nomes)
for y in range(n):
    print(y, alunos[y])
