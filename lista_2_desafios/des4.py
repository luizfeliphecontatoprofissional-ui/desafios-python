#caculadora
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
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opcao == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif opcao == '3':
        print(f"{num1} X {num2} = {num1 * num2}")
    elif opcao == '4':
        if num2 == 0:
            print("Erro: Não é possível dividir por zero")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")