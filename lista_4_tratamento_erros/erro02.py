def ler_preco():
    """
    Solicita e valida o preço de um produto, tratando ponto ou
    vírgula como separador decimal e tratando entradas não numéricas
    e valores menores ou iguais a zero.
    :return: Preço válido do produto (float).
    """
    while True:
        try:
            num = input("Digite o preço do produto: ")
            num = num.replace(",", ".")
            num = float(num)
            if num <= 0:
                print("Erro! O preço deve ser maior que zero.")
            else:
                return num
        except ValueError:
            print("Erro! Digite um valor numérico.")


num = ler_preco()
print(f"Preço registrado: R$ {num:.2f}")