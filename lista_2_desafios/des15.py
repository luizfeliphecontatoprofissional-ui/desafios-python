#Carrinho de Compras
from time import sleep
produtos = {}
while True:
    print("[1] Adicionar produto")
    print("[2] Ver lista de produtos")
    print("[3] Sair")
    escolha = int(input("Digite a sua escolha: "))

    if escolha == 1:
        nome_produto = input("Digite o nome do produto: ").strip()
        preco_produto = float(input("Digite o preço do produto: "))
        produtos[nome_produto] = preco_produto
        sleep(0.3)
        print(f"Produto {nome_produto} adicionado!\n")

    elif escolha == 2:
        if len(produtos) == 0:
            sleep(0.3)
            print("Nenhum produto cadastrado.")
        else:
            print("\n=== Lista de Produtos ===")
            for nome_produto, preco in produtos.items():
                sleep(0.3)
                print(f"{nome_produto} -> R$ {preco:.2f}")

            total = sum(produtos.values())
            sleep(0.3)
            print("------------------------------")
            sleep(0.5)
            print(f"Valor total: R$ {total:.2f}")
            sleep(0.2)
            print("==============================\n")

    elif escolha == 3:
        sleep(0.4)
        print("Saindo...")
        break
    elif escolha < 1 or escolha > 3:
        sleep(0.2)
        print("Opção inválida! Escolha um número de 1 a 3.\n")
        continue
