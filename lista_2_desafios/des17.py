#Sistema Bancário Simples
saldo = 0
from time import sleep
while True:
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Consultar saldo")
    print("[4] Sair")
    escolha = int(input("Digite a sua escolha (entre 1 a 4): "))

    if escolha == 4:
        sleep(0.2)
        print("Saindo...")
        sleep(0.3)
        break

    elif escolha < 1 or escolha > 4:
        sleep(0.2)
        print("Opção inválida! Escolha entre as opções de 1 a 4.\n")
        continue

    elif escolha == 1:
        deposito = float(input("Deposite uma quantidade de dinheiro: R$"))
        if deposito < 0:
            sleep(0.3)
            print("Não é permitido depósito negativo!")
        else:
            saldo += deposito
            sleep(0.4)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif escolha == 2:
        saque = float(input("Digite uma quantidade para ser sacada: R$"))
        if saque <= 0:
            sleep(0.2)
            print("Valor inválido para saque! Digite um valor maior do que zero.\n")
        elif saldo < saque:
            sleep(0.2)
            print(f"Seu saldo é de: R${saldo:.2f} | Seu saque foi de {saque:.2f}\n")
            print("Não foi possível realizar o saque.")
        else:
            saldo -= saque
            sleep(0.3)
            print(f"Saque de R${saque:.2f} realizado! Seu saldo atual é de {saldo:.2f}.")

    elif escolha == 3:
        sleep(0.2)
        print(f"Seu saldo atual é de: R${saldo:.2f}\n")