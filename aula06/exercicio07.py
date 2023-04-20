#perguntar ao usuario quantos alunos tem na sala e criar um array, unidimensional(vetor)com o nome de todos os alunos da sala

alunos= []
n = int(input("quantos alunos tem na sala? "))
for x in range(n):
    nomes = input("digite o nome do aluno: ")
    alunos.append(nomes)
    for y in alunos:
       print(y)



