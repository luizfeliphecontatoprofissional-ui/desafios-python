#Agenda de Contatos
agenda = {}

while True:
    print("[1] Adicionar contato")
    print("[2] Listar contatos")
    print("[3] Procurar contato")
    print("[4] Sair")
    escolha = int(input("Digite a escolha: "))

    if escolha == 1:
        nome = input("Digite o nome do contato: ").strip()
        telefone = input("Digite o número de telefone do contato: ").strip().title()
        agenda[nome] = telefone
        print(f"Contato de {nome} adicionado com sucesso!\n")
    elif escolha == 2:
        if len(agenda) == 0:
            print("A agenda está vazia!\n")
        else:
            print("\n=== Lista de Contatos ===")
            for nome, telefone in agenda.items():
                print(f"{nome} -> {telefone}")
            print("=========================\n")
    elif escolha == 3:
        nome_busca = input("Digite o nome que deseja procurar: ").strip().title()

        if nome_busca in agenda:
            print(f"Contato encontrado: {nome_busca} -> {agenda[nome_busca]}.\n")
        else:
            print(f"O contato '{nome_busca}' não foi encontrado na agenda.\n")

    if escolha == 4:
        print("Saindo...")
        break
    elif escolha < 1 or escolha > 4:
        print("Opção inválida! Escolha um número de 1 a 4.\n")
        continue
