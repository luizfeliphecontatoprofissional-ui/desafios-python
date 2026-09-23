print("--- Calculadora ---")

while True:
    print("0 - Sair\n1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir")
    opcao = input("Qual opção você escolhe? ")

    if opcao == '0':
        print("A encerrar o programa...")
        break

    if opcao not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
        continue

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if opcao == '1':
        soma = num1 + num2
        print(f"{num1} + {num2} = {soma}")
    elif opcao == '2':
        subtracao = num1 - num2
        print(f"{num1} - {num2} = {subtracao}")
    elif opcao == '3':
        multiplicacao = num1 * num2
        print(f"{num1} X {num2} = {multiplicacao}")
    elif opcao == '4':
        divisao = num1 / num2
        print(f"{num1} / {num2} = {divisao}")