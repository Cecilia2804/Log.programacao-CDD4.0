#ler as notas de uma turma de cinco alunos e guarde um vetor
#calcular media da turma e contar quantos alunos obtiveram nota na media
#escrever a media da turma e o resultado da contagem

nota = []
soma = 0
cont = 0
for x in range(5):
    nota.append(float(input("digite as notas do aluno: ")))
for y in range(5):
    soma = soma + nota[y]
media = soma / 5
print("a media da turma é", media)
for b in range(5):
    if nota[b] >= media:
     cont += 1
print(cont, "alunos conseguiram ficar na media!")

