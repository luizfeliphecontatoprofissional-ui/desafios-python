from time import sleep

despesas = []

def adicionar_despesa(despesas, descricao, categoria, valor):
    nova_despesa = {
        "descricao": descricao,
        "categoria": categoria,
        "valor": valor
    }

    despesas.append(nova_despesa)


def listar_despesas(despesas):
    if len(despesas) == 0:
        print("Nenhuma despesa cadastrada.")
    else:
        for despesa in despesas:
            print(f"Descrição: {despesa['descricao']}")
            print(f"Categoria: {despesa['categoria']}")
            print(f"Valor: R$ {despesa['valor']:.2f}")
            print('-' * 30)


def consultar_total(despesas):
    if len(despesas) == 0:
        sleep(1)
        print("Nenhuma despesa cadastrada. Nenhum valor total.")
    else:
        total = 0
        for despesa in despesas:
            total += despesa['valor']
        sleep(1)
        print(f'Total gasto: R$ {total:.2f}')


def consultar_categoria(despesas, categoria):
    if len(despesas) == 0:
        sleep(1)
        print("Nenhuma despesa cadastrada. Sem nenhuma categoria para ser consultada.")
    else:
        encontrou = False

        for despesa in despesas:
            if despesa['categoria'] == categoria:
                sleep(1)
                print(f"Descrição: {despesa['descricao']}")
                print(f"Categoria: {despesa['categoria']}")
                print(f"Valor: R$ {despesa['valor']:.2f}")

                encontrou = True

        if encontrou == False:
            print("Categoria não encontrada!")


def excluir_despesa(despesas):
    if len(despesas) == 0:
        sleep(1)
        print("Nenhuma despesa cadastrada.")
        return
    else:
        nome = input("Digite a descrição da despesa que deseja excluir: ").strip()

        for despesa in despesas:
            if despesa['descricao'] == nome:
                despesas.remove(despesa)
                sleep(1)
                print("Despesa removido com sucesso!")
                return
        print("Despesa não encontrada.")


while True:
    print("===== CONTROLE DE DESPESAS =====\n")
    sleep(0.35)
    print('[1] Adicionar despesa')
    print('[2] Listar despesas')
    print('[3] Consultar total gasto')
    print('[4] Consultar despesas por categoria')
    print('[5] Excluir despesa')
    print('[6] Sair')

    escolha = int(input("Digite sua escolha: "))

    if escolha > 6 or escolha < 1:
        print("Escolha uma opção válida.")
        continue

    if escolha == 6:
        sleep(1)
        print("Saindo...")
        break
    elif escolha == 1:
        descricao = input("Descrição da despesa: ").strip()
        categoria = input("Categoria da despesa: ").strip()
        valor = float(input("Valor da despesa: R$ "))

        if valor <= 0:
            print("O valor deve ser maior que zero.")
            continue

        adicionar_despesa(despesas, descricao, categoria, valor)
        print("Despesa cadastrada com sucesso!")

    elif escolha == 2:
        listar_despesas(despesas)

    elif escolha == 3:
        consultar_total(despesas)

    elif escolha == 4:
        categoria = input("Digite a categoria que deseja consultar: ").strip()
        consultar_categoria(despesas, categoria)

    elif escolha == 5:
        excluir_despesa(despesas)
