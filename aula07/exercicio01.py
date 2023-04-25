#altere o exercicio anterior (exercicio07) e mostre na tela, o nome de cada aluno e sua respectiva posição no array
alunos= []
n = int(input("quantos alunos tem na sala? "))
for x in range(n):
    nomes = input("digite o nome do aluno: ")
    alunos.append(nomes)
for y in range(n):
    print(y, alunos[y])
nome = input("digite o nome que deseja pesquisar: ")
cont = 0
for z in range(n):
    if alunos[z] == nome:
        print(z, alunos[z])
    else:
        cont += 1

if cont == n:
    print("não encontrado!")


