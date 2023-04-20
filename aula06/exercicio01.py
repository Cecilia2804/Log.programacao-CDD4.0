opcao=1

while opcao != 6:
    n1 = float(input("digite o primeiro numero: "))
    n2 = float(input("digite o segundo numero: "))
    while True:
        opcao = int(input(
            "1. soma\n"
            "2. subtracao\n"
            "3. multiplicacao\n"
            "4. divisao\n"
            "5. digitar um novo numero\n"
            "6. sair\n"
            "selecione uma opcao: "
        ))
        match opcao:
            case 1:
                print(n1, "+", n2, "=", n1 + n2)
            case 2:
                print(n1, "-", n2, "=", n1 - n2)
            case 3:
                print(n1, "*", n2, "=", n1 * n2)
            case 4:
                print(n1, "/", n2, "=", n1 / n2)
            case 5:
                break
            case 6:
                print("programa encerrado!")
                break
