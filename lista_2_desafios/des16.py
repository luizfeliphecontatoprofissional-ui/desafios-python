#Controle de Estoque
from time import sleep
estoque = {}
while True:
    print("[1] Adicionar produto")
    print("[2] Alterar quantidade")
    print("[3] Listar estoque")
    print("[4] Consultar produto")
    print("[5] Sair")
    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        produto = input("Digite o nome do produto: ").strip().title()
        quantidade = int(input("Digite a quantidade de produto: "))
        estoque[produto] = quantidade
        sleep(0.3)
        print(f"Produto {produto} adicionado!\n")

    elif escolha == 2:
        if len(estoque) == 0:
            sleep(0.3)
            print("O estoque está vazio!\n")
        else:
            produto = input("Digite o nome do produto que deseja alterar: ").strip().title()
            if produto in estoque:
                nova_qtd = int(input(f"Digite a nova quantidade para {produto}: "))
                estoque[produto] = nova_qtd
                sleep(0.3)
                print(f"Quantidade de '{produto}' alterada para {nova_qtd} com sucesso!\n")
            else:
                sleep(0.3)
                print(f"Produto '{produto}' não encontrado no estoque.\n")

    elif escolha == 3:
        if len(estoque) == 0:
            sleep(0.3)
            print("Nenhum produto cadastrado.")
        else:
            print("\n=== Lista de Produtos ===")
            for produto, qtd in estoque.items():
                sleep(0.3)
                print(f"{produto} -> {qtd}")
            print("=========================\n")

    elif escolha == 4:
        if len(estoque) == 0:
            sleep(0.3)
            print("O estoque está vazio!\n")
        else:
            produto_busca = input("Digite o nome do produto para consultar: ").strip().title()
            sleep(0.3)
            if produto_busca in estoque:
                print(f"Produto: {produto_busca} | Quantidade em estoque: {estoque[produto_busca]}\n")
            else:
                print(f"Produto '{produto_busca}' não foi encontrado no estoque.\n")

    elif escolha == 5:
        sleep(0.4)
        print("Saindo...")
        break

    elif escolha < 1 or escolha > 5:
        sleep(0.2)
        print("Opção inválida! Escolha um número de 1 a 5.\n")
        continue
