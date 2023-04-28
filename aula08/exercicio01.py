#faça um codigo para ler 5 nomes de usuarios e suas respectivas senhas, e aramzenar cada lista em um array diferente
#apos completar a digitaçao, imprimir, nome, senha e posiçao dos dados do array

nome = []
senha = []
for x in range(5):
    nome.append(input("digite um nome para o usuario: "))
    senha.append(input("digite sua senha: "))

for y in range(5):
    print(y, nome[y], senha[y])
    

