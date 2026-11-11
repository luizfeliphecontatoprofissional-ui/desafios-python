def cadastrar_pessoa(**dados):
    print("===== CADSATRO =====")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


cadastrar_pessoa(nome="Luiz", idade=18, cidade="Curitiba")
