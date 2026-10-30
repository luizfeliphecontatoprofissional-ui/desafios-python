#Cadastro de Produtos V2
produtos = []

while True:
    print("\n--- MENU DE PRODUTOS ---")
    print("[1] Cadastrar produto")
    print("[2] Listar produtos")
    print("[3] Procurar produto")
    print("[4] Alterar preço")
    print("[5] Alterar quantidade")
    print("[6] Remover produto")
    print("[7] Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

    if opcao == 1:
        print("\n--- NOVO CADASTRO ---")
        nome = input("Nome do produto: ").strip().title()
        preco = float(input("Preço (R$): "))
        quantidade = int(input("Quantidade: "))

        produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
        produtos.append(produto)
        print(f"Produto '{nome}' cadastrado com sucesso!")

    elif opcao == 2:
        print("\n--- LISTA DE PRODUTOS ---")
        if not produtos:
            print("Ainda não há produtos cadastrados.")
        else:
            for i, p in enumerate(produtos, start=1):
                print(f"{i}. {p['nome']} | Preço: R$ {p['preco']:.2f} | Qtd: {p['quantidade']}")

    elif opcao == 3:
        print("\n--- PROCURAR PRODUTO ---")
        busca = input("Digite o nome do produto que deseja procurar: ").strip().title()
        encontrado = False
        for p in produtos:
            if p['nome'] == busca:
                print(f"Encontrado! Nome: {p['nome']} | Preço: R$ {p['preco']:.2f} | Qtd: {p['quantidade']}")
                encontrado = True
                break
        if not encontrado:
            print(f"Produto '{busca}' não foi encontrado.")

    elif opcao == 4:
        print("\n--- ALTERAR PREÇO ---")
        busca = input("Nome do produto cujo preço deseja alterar: ").strip().title()
        encontrado = False
        for p in produtos:
            if p['nome'] == busca:
                novo_preco = float(input(f"Novo preço para {p['nome']} (R$): "))
                p['preco'] = novo_preco
                print("Preço alterado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == 5:
        print("\n--- ALTERAR QUANTIDADE ---")
        busca = input("Nome do produto cuja quantidade deseja alterar: ").strip().title()
        encontrado = False
        for p in produtos:
            if p['nome'] == busca:
                nova_qtd = int(input(f"Nova quantidade para {p['nome']}: "))
                p['quantidade'] = nova_qtd
                print("Quantidade alterada com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == 6:
        print("\n--- REMOVER PRODUTO ---")
        busca = input("Nome do produto que deseja remover: ").strip().title()
        encontrado = False
        for p in produtos:
            if p['nome'] == busca:
                produtos.remove(p)
                print(f"Produto '{busca}' removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Produto não encontrado.")

    elif opcao == 7:
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida! Escolha um número entre 1 e 7.")