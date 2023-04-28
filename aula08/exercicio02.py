
nome = []
senha = []
cont = 0
for x in range(2):
    nome.append(input("digite um nome para o usuario: "))
    senha.append(input("digite sua senha: "))
login = (input("digite seu login de acesso: "))
pin = (input("digite a senha da sua conta: "))
for y in range(2):
    if login == nome[y] and pin == senha[y]:
        print("acesso liberado")
        break
    else:
        cont += 1
if cont == 5:
    print("acesso negado!, usuario nao encontrado")





