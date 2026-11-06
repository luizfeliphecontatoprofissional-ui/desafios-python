def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):

    return a / b


def calculadora(opcao, a, b):
    if opcao == 1:
        return somar(a, b)
    elif opcao == 2:
        return subtrair(a, b)
    elif opcao == 3:
        return multiplicar(a, b)
    elif opcao == 4:
        return dividir(a, b)


while True:
    print("\n--- Calculadora ---")
    print("[1] - Somar")
    print("[2] - Subtrair")
    print("[3] - Multiplicar")
    print("[4] - Divisão")
    print("[5] - Sair")

    escolha = int(input("Escolha: "))

    if escolha == 5:
        break

    if escolha < 1 or escolha > 5:
        print("Digite uma opção válida!")
        continue

    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    if escolha == 4 and num2 == 0:
        print("Não é possível dividir por zero!")
        continue

    resultado = calculadora(escolha, num1, num2)
    print(f"Resultado: {resultado}")