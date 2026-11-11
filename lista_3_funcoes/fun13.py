def leia_int(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Erro! Digite um número inteiro válido.")


num = leia_int("Digite um número: ")
print(f"Você digitou: {num}")
